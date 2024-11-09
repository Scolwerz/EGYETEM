<?php

function decrypt($data, $keys) {
    $decrypted_data = '';
    $key_length = count($keys);
    $key_index = 0;

    for ($i = 0; $i < strlen($data); $i++) {
        if ($data[$i] !== "\x0A") {
            $offset = $keys[$key_index % $key_length];
            $decoded_char = chr(ord($data[$i]) - $offset);

            // Ha kisebb, mint 32 (nem nyomtatható) - nem módosítjuk
            if (ord($decoded_char) < 32) {
                $decrypted_data .= $data[$i];
            }
            else { $decrypted_data .= $decoded_char; }
        }
        else {
            // Ha EOL karakter
            $decrypted_data .= $data[$i];
            $key_index = 0;
        }
        $key_index++;
    }
    return $decrypted_data;
}


function color($color) {
    switch ($color) {
        case "piros":  return "red";    break;
        case "zold":   return "green";  break; 
        case "sarga":  return "yellow"; break;
        case "kek":    return "blue";   break;
        case "fekete": return "black";  break;
        case "feher":  return "white";  break;
        default:       return "orange"; break;
    }
}






$servername = "localhost";
$dbusername = "webes2_adatok";
$dbpassword = "webes2_adatok_jelszo";
$dbname = "tabla";

$conn = new mysqli($servername, $dbusername, $dbpassword, $dbname);
if ($conn->connect_error) { die("Kapcsolódási hiba: " . $conn->connect_error); }

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'];
    $password = $_POST['password'];

    $passwords = file_get_contents("password.txt");
    $decrypted_passwords = decrypt($passwords, [5, -14, 31, -9, 3]);
    $lines = explode("\n", $decrypted_passwords);
    $found = false;
    foreach ($lines as $line) {
        $parts = explode("*", $line);
        $stored_username = $parts[0];
        $stored_password = $parts[1];
        if ($stored_username == $username && $stored_password == $password) {
            $found = true;
            break;
        }
    }

    // Ha megtaláltuk a megfelelő felhasználót és jelszót
    if ($found) {
        $sql = "SELECT Titkos FROM tabla WHERE Username='$username'";
        $result = $conn->query($sql);

        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $color = color($row["Titkos"]);
            echo "<body style='background: linear-gradient($color, black);'>";
        }
    }
	else if (empty($username)) { echo "Hiányzó felhasználónév!"; }
	else if (empty($password)) { echo "Hiányzó jelszó!"; }
	else {
        echo "Hibás felhasználónév vagy jelszó!";
        header("refresh:3;url=police.hu");
        }
    }
$conn->close();

?>


<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="styles.css">
	<title>Sign In</title>
</head>
<body>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <input type="text" name="username" value="Username">
		<br>
        <input type="password" name="password" value="Password">
		<br>
        <input type="submit" value="Sign In">
    </form>
</body>
</html>
