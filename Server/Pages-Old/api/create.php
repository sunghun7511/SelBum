<?php
    include_once("api.php");
    function d400($text) {
        http_response_code(400);
        die($text);
    }

    function d401($text) {
        http_response_code(401);
        die($text);
    }

    $albumname = $_POST['albumname'];
    $personalpicturecount = (int)$_POST['personalpicturecount'];
    $usepersonaldescription = (bool)$_POST['usepersonaldescription'];
    $accesstoken = $_POST['accesstoken'];

    if(!isset($albumname))
        d400("albumname not found");
    
    if(!isset($personalpicturecount))
        d400("personalpicturecount not found");
    
    
    $username = getUsernameFromAccessToken($accesstoken);
    if($username == NULL){

    }


?>