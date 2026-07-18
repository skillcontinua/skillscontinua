<?php
declare(strict_types=1);

function sc_config(): array {
  $path = __DIR__ . '/config/local.php';
  if (!is_file($path)) {
    throw new RuntimeException("Missing config: {$path}");
  }
  $cfg = require $path;
  if (!is_array($cfg)) {
    throw new RuntimeException("Invalid config file: {$path}");
  }
  return $cfg;
}

function sc_db(): PDO {
  static $pdo = null;
  if ($pdo instanceof PDO) return $pdo;

  $cfg = sc_config()['db'] ?? null;
  if (!is_array($cfg)) {
    throw new RuntimeException("Missing db config.");
  }

  $host = (string)($cfg['host'] ?? '127.0.0.1');
  $port = (int)($cfg['port'] ?? 5432);
  $name = (string)($cfg['name'] ?? '');
  $user = (string)($cfg['user'] ?? '');
  $pass = (string)($cfg['pass'] ?? '');

  if ($name === '' || $user === '') {
    throw new RuntimeException("DB name/user not configured.");
  }

  $dsn = "pgsql:host={$host};port={$port};dbname={$name}";
  $pdo = new PDO($dsn, $user, $pass, [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
  ]);

  return $pdo;
}
