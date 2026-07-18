<?php
declare(strict_types=1);

require_once __DIR__ . '/../app/db.php';

header('Content-Type: text/plain; charset=utf-8');

try {
  $pdo = sc_db();
  $v = $pdo->query("SELECT version() AS v")->fetch();
  echo "DB OK\n";
  echo $v['v'] . "\n";
} catch (Throwable $e) {
  http_response_code(500);
  echo "DB FAIL\n";
  echo $e->getMessage() . "\n";
}
