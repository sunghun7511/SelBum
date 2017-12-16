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
<<<<<<< HEAD
=======
    

    function login($username, $password) {
        $password = hash_password($password);

        $query = "select * from User where username='{$username}' and phash='{$password}";
        $result = mysqli_query($sql_conn, $query);
        $rows = mysqli_fetch_array($result);
        if(isset($rows['username'])) {
            return "";
        } else {
            return FALSE;
        }
    }

    
>>>>>>> d50ad2faee4b170bb019404b7f653c5026234449
?>