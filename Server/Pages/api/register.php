<?php
    include_once("api.php");
    $username = $_POST['username'];
    $password = $_POST['password']; 
    $nickname = $_POST['nickname'];
    $email = $_POST['email'];

    $queryLogin = "select * from Users where username='{$username}' and password='{$password}'";
    $queryLoginResult = mysqli_query($sql_conn, $queryLogin);
    $queryLoginArray = mysqli_fetch_array($queryLoginResult);

    function d400($text){
        http_response_code(400);
        die($text);
    }

    if(isset($queryLoginArray['username']))
        d400("");
    
    if(!isset($username))
        d400("");
    
    if(!isset($password)){

    }
    if(!isset($nickname)){

    }
    if(!isset($email)) {
    }
    $queryRegister = "insert into ('username', 'password', 'nickname', 'email') values ('{$username}', '{$password}', '{$nickname}', '{$email}')";
    mysqli_query($sql_conn, $queryRegister);
    http_response_code(200);
    die("");
?>