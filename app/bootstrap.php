<?php
// /app/bootstrap.php

declare(strict_types=1);

@ini_set('display_errors', '0');
@ini_set('display_startup_errors', '0');
error_reporting(E_ALL);

require_once __DIR__ . '/helpers.php';
require_once __DIR__ . '/db.php';

sc_session_start();

set_exception_handler(function (Throwable $e): void {
  http_response_code(500);
  header('Content-Type: text/plain; charset=utf-8');
  echo "SkillsContinua error\n";
  echo $e->getMessage() . "\n";
});
