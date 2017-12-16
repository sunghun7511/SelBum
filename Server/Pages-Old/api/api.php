<?php
    $sql_conn = mysqli_connect("localhost", "username", "password", "SelBum");

    header("Content-Type: application/json");
    header("Access-Control-Allow-Origin: *");
    header("charset=utf-8");

    function hash_password($password) {
        return hash('sha512', $password);
    }

    function __generate_random_uuid() {
        return sprintf( '%04x%04x-%04x%04x-%04x%04x-%04x%04x',
            mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ),
            mt_rand( 0, 0xffff ),
            mt_rand( 0, 0x0fff ) | 0x4000,
            mt_rand( 0, 0x3fff ) | 0x8000,
            mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff ), mt_rand( 0, 0xffff )
        );
    }

    function isValidID($username){
        if(strlen($username) < 5 || strlen($username) > 30){
            return false;
        }
        return true;
    }

    function isValidPassword($password){
        if(strlen($password) < 5 || strlen($password) > 30){
            return false;
        }
        return true;
    }

    function getAccessToken($username){

        $queryToken = "SELECT * FROM AccessToken WHERE username='{$username}'";
        $queryTokenResult = mysqli_query($sql_conn, $queryToken);
        $queryTokenArray = mysqli_fetch_array($queryTokenResult);

        if(isset($queryTokenArray)){
            return $queryTokenArray["accesstoken"];
        }

        $uuid = __generate_random_uuid();
        
        $queryInsertToken = "INSERT INTO AccessToken (username, accesstoken) VALUES('{$username}', '{$uuid}')"
        mysqli_query($sql_conn, $queryInsertToken);

        return $uuid;
    }

    function getUsernameFromAccessToken($access_token){
        $queryToken = "SELECT * FROM AccessToken WHERE accesstoken='{$access_token}'";
        $queryTokenResult = mysqli_query($sql_conn, $queryToken);
        $queryTokenArray = mysqli_fetch_array($queryTokenResult);

        if(isset($queryTokenArray)){
            return $queryTokenArray["username"];
        }

        return NULL;
    }

    function d400($text){
        http_response_code(400);
        die($text);
    }
    
    function d200($text){
        http_response_code(200);
        die($text);
    }

    function d401($text){
        http_response_code(401);
        die($text);
    }
?>