<?php
declare(strict_types=1);

require_once __DIR__ . '/../../app/auth.php';

sc_logout();
sc_redirect('/skillscontinua/auth/login.php');
