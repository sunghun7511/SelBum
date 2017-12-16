# Server Plan
- This project follow RESTFul API

# API definitation
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /login | send login request | POST | username - String <br> password - String | 200 OK <br/> 403 Forbidden | None |
| /register | send register request | POST | username - String <br> password - String <br> nickname - String <br> email - String | 200 OK <br> 403 Forbidden | If Response code is 403, fail message

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
| uid         | INT         | UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT |
| name        | CHAR(50)    | NOT NULL                                     |
| 