<?php
declare(strict_types=1);

/**
 * /public/admin/bootstrap.php
 * One-time bootstrap: creates first admin user + assigns admin role.
 *
 * SECURITY:
 * - Requires a shared secret (SC_BOOTSTRAP_KEY) set below.
 * - Refuses to run if any admin already exists.
 * - Deletes itself after success (if filesystem permits).
 *
 * After success:
 * - Login at /skillscontinua/auth/login.php
 * - Then DELETE this file manually if auto-delete fails.
 */

require_once __DIR__ . '/../../app/auth.php';

define('SC_BOOTSTRAP_KEY', 'chandigarh153547nkwerre19'); // <-- change this

header('Content-Type: text/plain; charset=utf-8');

$method = strtoupper((string)($_SERVER['REQUEST_METHOD'] ?? 'GET'));
$key = (string)($_GET['k'] ?? $_POST['k'] ?? '');

if (!hash_equals(SC_BOOTSTRAP_KEY, $key)) {
  http_response_code(403);
  echo "Forbidden\n";
  echo "Provide correct key via ?k=...\n";
  exit;
}

$pdo = sc_db();

/* 1) If admin already exists, refuse */
$adminExists = (int)$pdo->query("
  SELECT 1
  FROM user_roles ur
  JOIN roles r ON r.id = ur.role_id
  WHERE r.code = 'admin'
  LIMIT 1
")->fetchColumn();

if ($adminExists === 1) {
  http_response_code(409);
  echo "Admin already exists. Bootstrap refused.\n";
  exit;
}

/* 2) Collect inputs (GET for quick use; POST supported) */
$email = trim((string)($_GET['email'] ?? $_POST['email'] ?? ''));
$name  = trim((string)($_GET['name']  ?? $_POST['name']  ?? ''));
$pw    = (string)($_GET['pw'] ?? $_POST['pw'] ?? '');

if ($email === '' || $name === '' || $pw === '') {
  echo "Usage:\n";
  echo "  /skillscontinua/admin/bootstrap.php?k=YOUR_KEY&email=ihenuzu@gmail.com&name=Theophilus&pw=chandigarh153547nkwerre19\n";
  exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  http_response_code(400);
  echo "Invalid email.\n";
  exit;
}

if (strlen($pw) < 10) {
  http_response_code(400);
  echo "Password too short (min 10 chars).\n";
  exit;
}

$hash = password_hash($pw, PASSWORD_DEFAULT);
if (!$hash) {
  http_response_code(500);
  echo "Failed to hash password.\n";
  exit;
}

/* 3) Ensure admin role exists */
$pdo->exec("INSERT INTO roles(code, name) VALUES ('admin','Administrator') ON CONFLICT (code) DO NOTHING");

/* 4) Create user + assign role in a transaction */
$pdo->beginTransaction();
try {
  $st = $pdo->prepare("
    INSERT INTO users(email, full_name, password_hash, is_active)
    VALUES (:email, :name, :hash, TRUE)
    RETURNING id
  ");
  $st->execute([':email' => $email, ':name' => $name, ':hash' => $hash]);
  $uid = (int)$st->fetchColumn();

  $st2 = $pdo->prepare("
    INSERT INTO user_roles(user_id, role_id)
    SELECT :uid, r.id FROM roles r WHERE r.code='admin'
    ON CONFLICT DO NOTHING
  ");
  $st2->execute([':uid' => $uid]);

  $pdo->commit();
} catch (Throwable $e) {
  $pdo->rollBack();
  http_response_code(500);
  echo "Bootstrap failed: " . $e->getMessage() . "\n";
  exit;
}

/* 5) Attempt self-delete */
$me = __FILE__;
$deleted = @unlink($me);

echo "OK: Admin created.\n";
echo "Email: {$email}\n";
echo "Login: /skillscontinua/auth/login.php\n";
echo $deleted ? "Bootstrap file deleted.\n" : "IMPORTANT: Delete this file manually: {$me}\n";
