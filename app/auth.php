<?php
declare(strict_types=1);

require_once __DIR__ . '/bootstrap.php';

function sc_current_user(): ?array {
  sc_session_start();
  $uid = (int)($_SESSION['uid'] ?? 0);
  if ($uid <= 0) return null;

  $pdo = sc_db();
  $st = $pdo->prepare("SELECT id, email, phone, full_name, is_active FROM users WHERE id = :id LIMIT 1");
  $st->execute([':id' => $uid]);
  $u = $st->fetch();
  if (!$u || empty($u['is_active'])) return null;
  return $u;
}

function sc_user_has_role(int $userId, string $roleCode): bool {
  $pdo = sc_db();
  $st = $pdo->prepare("
    SELECT 1
    FROM user_roles ur
    JOIN roles r ON r.id = ur.role_id
    WHERE ur.user_id = :uid AND r.code = :code
    LIMIT 1
  ");
  $st->execute([':uid' => $userId, ':code' => $roleCode]);
  return (bool)$st->fetchColumn();
}

function sc_require_login(): array {
  $u = sc_current_user();
  if (!$u) sc_redirect('/skillscontinua/auth/login.php');
  return $u;
}

function sc_require_role(string $roleCode): array {
  $u = sc_require_login();
  if (!sc_user_has_role((int)$u['id'], $roleCode)) {
    http_response_code(403);
    header('Content-Type: text/plain; charset=utf-8');
    echo "Forbidden\n";
    exit;
  }
  return $u;
}

function sc_attempt_login(string $identifier, string $password): ?array {
  $id = trim($identifier);
  if ($id === '' || $password === '') return null;

  $pdo = sc_db();
  $st = $pdo->prepare("
    SELECT id, email, phone, full_name, password_hash, is_active
    FROM users
    WHERE (email = :id OR phone = :id)
    LIMIT 1
  ");
  $st->execute([':id' => $id]);
  $u = $st->fetch();
  if (!$u || empty($u['is_active'])) return null;

  if (!password_verify($password, (string)$u['password_hash'])) return null;

  sc_session_start();
  session_regenerate_id(true);
  $_SESSION['uid'] = (int)$u['id'];

  return $u;
}

function sc_logout(): void {
  sc_session_start();
  $_SESSION = [];
  if (ini_get("session.use_cookies")) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000, $p["path"], $p["domain"], (bool)$p["secure"], (bool)$p["httponly"]);
  }
  session_destroy();
}
