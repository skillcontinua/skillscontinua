<?php
declare(strict_types=1);

require_once __DIR__ . '/../app/bootstrap.php';

echo "<h1>SkillsContinua</h1>";
echo "<p>Local app bootstrap OK.</p>";

try {
  $pdo = sc_db();
  $v = $pdo->query("SELECT version() AS v")->fetch();
  echo "<pre>" . htmlspecialchars($v['v'] ?? '', ENT_QUOTES, 'UTF-8') . "</pre>";
} catch (Throwable $e) {
  echo "<pre>DB not available: " . htmlspecialchars($e->getMessage(), ENT_QUOTES, 'UTF-8') . "</pre>";
}
