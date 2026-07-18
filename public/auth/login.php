<?php
declare(strict_types=1);

require_once __DIR__ . '/../../app/auth.php';

$method = strtoupper((string)($_SERVER['REQUEST_METHOD'] ?? 'GET'));
$err = '';

if ($method === 'POST') {
  $csrf = (string)($_POST['csrf'] ?? '');
  if (!sc_csrf_check($csrf)) {
    $err = 'CSRF failed. Refresh and try again.';
  } else {
    $id = (string)($_POST['id'] ?? '');
    $pw = (string)($_POST['pw'] ?? '');
    $u = sc_attempt_login($id, $pw);
    if ($u) {
      sc_redirect('/skillscontinua/admin/');
    }
    $err = 'Invalid login.';
  }
}

?>
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SkillsContinua — Login</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <h1>SkillsContinua</h1>
  <h2>Staff Login</h2>

  <?php if ($err): ?>
    <p style="color:#b00020;"><?php echo h($err); ?></p>
  <?php endif; ?>

  <form method="post" action="">
    <input type="hidden" name="csrf" value="<?php echo h(sc_csrf_token()); ?>">
    <div>
      <label>Email or phone</label><br>
      <input name="id" autocomplete="username" required>
    </div>
    <div style="margin-top:10px;">
      <label>Password</label><br>
      <input name="pw" type="password" autocomplete="current-password" required>
    </div>
    <div style="margin-top:12px;">
      <button type="submit">Login</button>
    </div>
  </form>
</body>
</html>
