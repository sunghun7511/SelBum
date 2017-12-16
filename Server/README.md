# Server Plan
- This project follow RESTFul API

# API definitation
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /login | send login request | POST | username - String <br> password - String | 200 OK <br/> 403 Forbidden | None |
| /register | send register request | POST | username - String <br> password - String <br> nickname - String <br> email - String | 200 OK <br> 403 Forbidden | If response code is 403, fail message |
| /create | create new album | POST | albumname - String | 200 OK <br> 403 Forbidden | If response code is 403, fail message |
| /addpicture | add new picture | POST | albumname - String <br> picture - File <br> 

# Database Schema definition
## User
| Column      | Type        | Options               |
| :---------- | ----------- | --------------------- |
| username    | CHAR(30)    | NOT NULL PRIMARY KEY  |
| nickname    | CHAR(30)    | NOT NULL UNIQUE       |
| email       | CHAR(50)    | NOT NULL UNIQUE       |
| phash       | CHAR(128)   | NOT NULL              |

## Album
| Column      | Type        | Options                                      |
| :---------- | ----------- | -------------------------------------------- |
| uid         | INT(11)     | UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT |
| name        | CHAR(50)    | NOT NULL                                     |

## Role
### Table
| Column      | Type        | Options         |
| :---------- | ----------- | --------------- |
| username    | CHAR(30)    | NOT NULL UNIQUE |
| role        | INT(11)     | NOT NULL        |
### Options
INDEX(username),
FOREIGN KEY(username) REFRENCES User(username) ON UPDATE CASCADE ON DELETE CASCADE