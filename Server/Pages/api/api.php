<?php
    include_once("./db.php");
    function hash_password($password) {
        return hash('sha512', $password);
    }

    function generate_AccessToken(){
        return "adsafasdf";
    }

    function getUsernameFromAccessToken($access_token){
        return "username";
    }


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
?>