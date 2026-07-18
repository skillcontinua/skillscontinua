<?php
declare(strict_types=1);

require_once __DIR__ . '/../../app/auth.php';

$me = sc_require_role('admin');

?>
<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>SkillsContinua — Admin</title></head>
<body>
  <h1>Admin</h1>
  <p>Welcome, <?php echo h((string)$me['full_name']); ?></p>
  <p><a href="/skillscontinua/auth/logout.php">Logout</a></p>

  <ul>
    <li><a href="/skillscontinua/admin/programs.php">Programs</a> (next)</li>
    <li><a href="/skillscontinua/admin/courses.php">Courses</a> (next)</li>
  </ul>
</body>
</html>
