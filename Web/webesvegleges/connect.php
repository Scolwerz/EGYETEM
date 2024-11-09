<?php 

$json_file = "config.json";
$json_read = file_get_contents($json_file);
$json_decode = json_decode($json_read, true);


$host = $json_decode['host'];
$user = $json_decode['user'];
$password = $json_decode['password'];
$database = $json_decode['database_name'];


try {

    $connect = new mysqli($host, $user, $password, $database);

} catch (Exception $e) {

    die("Hiba a kapcsolat létrehozásakor: " . $e->getMessage());
}
?>