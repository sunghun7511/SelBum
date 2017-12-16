<?php
    include_once("api.php");
    include_once("db.php");
    $username = $_POST['username'];
    $password = $_POST['password']; 
    $nickname = $_POST['nickname'];
    $email = $_POST['email'];

    $checkEmail = filter_var($email, FILTER_VARIDATE_EMAIL);

    $queryLogin = "select * from Users where username='{$username}' and password='{$password}'";
    $queryLoginResult = mysqli_query($sql_conn, $queryLogin);
    $queryLoginArray = mysqli_fetch_array($queryLoginResult);


    if(isset($queryLoginArray['username']))
        d400("already defined username");
    
    if(!isset($username))
        d400("username not found");

    if(!isset($password))
        d400("password not found");

    if(!isset($nickname))
        d400("nickname not found");

    if(!isset($email)) 
        d400("email not found");
    
    if($checkEmail == FALSE)
        d400("synatx error email");

    $queryRegister = "insert into ('username', 'password', 'nickname', 'email') values ('{$username}', '{$password}', '{$nickname}', '{$email}')";
    mysqli_query($sql_conn, $queryRegister);
    http_response_code(200);
    die(generate_AccessToken());
?>