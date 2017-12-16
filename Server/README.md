# Server Plan
- This project follow RESTFul API

# API definitation
## URI
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /api/login.php | send login request | POST | username - String <br> password - String | 200 OK <br/> 400 Bad Request | 200 Access Token <br> 403 None |
| /api/register.php | send register request | POST | username - String <br> password - String <br> nickname - String <br> email - String | 200 OK <br> 400 Bad Request | 200 Access Token <br> 403 fail message |
| /api/create.php | create new album | POST | albumname - String <br> personalpicturecount - int <br> usepersonaldescription - Boolean <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized  | 200 Album uid <br> 400 Fail message <br> 401 None |
| /api/setrole.php | set role(Only admin) | POST | albumname - String <br> username - String <br> role - RoleType <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None
| /api/getrole.php | get role | POST | albumname - String <br> username - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 RoleType <br> 400 Fail message <br> 401 None
| /api/addpicture.php | add new picture | POST | albumname - String <br> foldertype - FolderType <br> picture - File <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None
| /api/setpersonalpicturecount.php | set personal picture count | POST | albumname - String <br> count - int <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None
| /api/setpersonaldescriptionuse.php | set personal description use flag | POST | albumname - String <br> flag - Boolean <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None
| /api/getpicturelist.php | get picture list | POST | albumname - String <br> foldertype - FolderType <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 picture path list (Type : JSON) <br> 400 Fail message <br> 401 None
| /api/getpictureinfo.php | get picture | POST | albumname - String <br> foldertype - FolderType <br> picturepath - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 picture info (Type : JSON) <br> 400 Fail message <br> 401 None
| /api/setdescription.php | set description | POST | albumname - String <br> foldertype - FolderType <br> description - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None

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

### Boolean
| Flag   | rawdata  |
| :----- | -------- |
| False  | 0        |
| True   | 1(not 0) |

## Examples
### getpictureinfo.php
#### Request


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