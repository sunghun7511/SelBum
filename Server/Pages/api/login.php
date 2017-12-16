<?php

include_once("auths.php");
$username = $_POST['username'];
$password = $_POST['password'];
if(login($username, $password) == TRUE)
{
    http_response_code(200);
    die(generate_AccessToken());    
}

else
{
    http_response_code(403);
    die("None");
}
?>