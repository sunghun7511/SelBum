# Server Plan
- This project follow RESTFul API

# API definitation
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /login | send login request | POST | id - String <br> pw - String | 200 OK <br/> 403 Forbidden | None |
| /register | send register request | POST | id - String <br> pw - String <br> nickname - String <br> email - String | 200 OK <br> 403 Forbidden | If Response code is 403, fail message

# Schema definition
## User
| Column      | Type        | Options               |
| :---------- | ----------- | --------------------- |
| username    | CHAR(30)    | NOT NULL PRIMARY KEY  |
| nickname    | CHAR(30)    | NOT NULL UNIQUE       |
| email       | CHAR(50)    | NOT NULL UNIQUE       |
| phash       | CHAR(128)   | NOT NULL              |