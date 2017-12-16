<?php
    include_once("./db.php");

    header("Content-Type: application/json");
    header("Access-Control-Allow-Origin: *");
    header("charset=utf-8");

    function hash_password($password) {
        return hash('sha512', $password);
    }

    function generate_AccessToken(){
        return "adsafasdf";
    }

    function getUsernameFromAccessToken($access_token){
        return "username";
    }
?>