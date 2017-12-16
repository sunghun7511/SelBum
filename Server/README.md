# Server Plan
- This project follow RESTFul API

# API definitation
## URI
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /api/login.php | send login request | POST | username - String <br> password - String | 200 OK <br/> 403 Forbidden | 200 Access Token <br> 403 None |
| /api/register.php | send register request | POST | username - String <br> password - String <br> nickname - String <br> email - String | 200 OK <br> 403 Forbidden | 200 Access Token <br> 403 fail message |
| /api/create.php | create new album | POST | albumname - String <br> accesstoken - String | 200 OK <br> 401 Unauthorized <br> 403 Forbidden  | 200 Album uid <br> 401 None <br> 403 fail message |
| /api/setrole.php | set role(Only admin) | POST | albumname - String <br> username - String <br> role - RoleType <br> accesstoken - String | 200 OK <br> 401 Unauthorized <br> 403 Forbidden | 200 None <br> 401 None <br> 403 fail message
| /api/getrole.php | get role | POST | albumname - String <br> username - String <br> accesstoken - String | 200 OK <br> 401 Unauthorized <br> 403 Forbidden | 200 RoleType <br> 401 None <br> 403 fail message
| /api/addpicture.php | add new picture | POST | albumname - String <br> picture - File <br> accesstoken - String | 200 OK <br> 401 Unauthorized <br> 403 Forbidden | 200 None <br> 401 None <br> 403 fail message

## Structures
### RoleType
| Role  | rawdata |
| :---- | ------- |
| User  | 0       |
| Admin | 1       |

### FolderType
| Folder    | rawdata |
| :-------- | ------- |
| Personal  | 0       |
| Class     | 1       |
| Event     | 2       |

# Database Schema definition
## User
| Column      | Type        | Options               |
| :---------- | ----------- | --------------------- |
| username    | CHAR(30)    | NOT NULL PRIMARY KEY  |
| nickname    | CHAR(30)    | NOT NULL UNIQUE       |
| email       | CHAR(50)    | NOT NULL UNIQUE       |
| phash       | CHAR(128)   | NOT NULL              |

## Album
| Column                 | Type        | Options                                      |
| :--------------------- | ----------- | -------------------------------------------- |
| uid                    | INT(11)     | UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT |
| name                   | CHAR(50)    | NOT NULL                                     |
| personalCount          | INT(11)     | UNSIGNED NOT NULL                            |
| usePersonalDescription | INT(11)     | UNSIGNED NOT NULL DEFAULT(0)                 |

## Role
| Column      | Type        | Options           |
| :---------- | ----------- | ----------------- |
| username    | CHAR(30)    | NOT NULL UNIQUE   |
| albumuid    | INT(11)     | UNSIGNED NOT NULL |
| role        | INT(11)     | NOT NULL          |

## Pictures
| Column      | Type        | Options           |
| :---------- | ----------- | ----------------- |
| filename    | CHAR(30)    | NOT NULL UNIQUE   |
| owner       | CHAR(30)    | NOT NULL          |
| albumuid    | INT(11)     | UNSIGNED NOT NULL |
| foldertype  | INT(11)     | UNSIGNED NOT NULL |
| priority    | INT(11)     | UNSIGNED NOT NULL |
| description | CHAR(300)   | |