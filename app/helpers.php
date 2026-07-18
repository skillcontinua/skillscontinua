<?php
declare(strict_types=1);

function h(string $v): string {
  return htmlspecialchars($v, ENT_QUOTES, 'UTF-8');
}

function sc_redirect(string $to): never {
  header('Location: ' . $to, true, 302);
  exit;
}

function sc_session_start(): void {
  if (session_status() === PHP_SESSION_ACTIVE) return;
  // Secure-ish defaults for local; adjust for prod later
  @ini_set('session.use_strict_mode', '1');
  @session_start();
}

function sc_csrf_token(): string {
  sc_session_start();
  if (empty($_SESSION['csrf'])) {
    $_SESSION['csrf'] = bin2hex(random_bytes(32));
  }
  return (string)$_SESSION['csrf'];
}

function sc_csrf_check(?string $token): bool {
  sc_session_start();
  $t = (string)($token ?? '');
  return $t !== '' && isset($_SESSION['csrf']) && hash_equals((string)$_SESSION['csrf'], $t);
}
