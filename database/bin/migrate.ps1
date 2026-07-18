param(
  [string]$DbHost = "127.0.0.1",
  [int]$DbPort = 5432,
  [string]$DbName = "skillscontinua",
  [string]$DbUser = "sc_app"
)

$ErrorActionPreference = "Stop"

Write-Host "== SkillsContinua migrations =="

# prompt for password securely
$pw = Read-Host -AsSecureString "Password for $DbUser"
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pw)
$plain = [System.Runtime.InteropServices.Marshal]::PtrToStringBSTR($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

$env:PGPASSWORD = $plain

try {
  $migrationsDir = "C:\skillscontinua\database\migrations"

  # ensure meta table exists
  $initSql = @"
CREATE TABLE IF NOT EXISTS sc_migrations (
  id BIGSERIAL PRIMARY KEY,
  filename TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
"@

  psql -U $DbUser -h $DbHost -p $DbPort -d $DbName -v ON_ERROR_STOP=1 -q -c $initSql | Out-Null

  $files = Get-ChildItem $migrationsDir -Filter "*.sql" | Sort-Object Name

  foreach ($f in $files) {
    $already = psql -U $DbUser -h $DbHost -p $DbPort -d $DbName -At -q `
      -c "SELECT 1 FROM sc_migrations WHERE filename='$($f.Name)' LIMIT 1;" 2>$null

    if ($already -eq "1") {
      Write-Host "SKIP  $($f.Name)"
      continue
    }

    Write-Host "APPLY $($f.Name)"
    psql -U $DbUser -h $DbHost -p $DbPort -d $DbName -v ON_ERROR_STOP=1 -q -f $f.FullName | Out-Null
    psql -U $DbUser -h $DbHost -p $DbPort -d $DbName -v ON_ERROR_STOP=1 -q `
      -c "INSERT INTO sc_migrations(filename) VALUES('$($f.Name)');" | Out-Null
  }

  Write-Host "DONE"
}
finally {
  Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
}
