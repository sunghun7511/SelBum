# Server Plan
- This project use REST API

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

## AccessToken
| Column      | Type        | Options           |
| :---------- | ----------- | ----------------- |
| username    | CHAR(30)    | NOT NULL UNIQUE   |
| accesstoken | CHAR(35)    | NOT NULL UNIQUE   |