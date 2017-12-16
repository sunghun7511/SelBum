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
| Column      | Type    | Options               |
| :---------- | ------- | --------------------- |
| username    | TEXT    | NOT NULL PRIMARY KEY  |
| nickname    | TEXT    | NOT NULL UNIQUE       |
| email       | TEXT    | NOT NULL UNIQUE       |
| phash       | TEXT    | NOT NULL              |

```
CREATE TABLE IF NOT EXISTS User (username TEXT PRIMARY KEY NOT NULL, nickname TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, phash TEXT NOT NULL)
```

## Album
| Column                 | Type        | Options                              |
| :--------------------- | ----------- | ------------------------------------ |
| uid                    | INTEGER     | PRIMARY KEY AUTOINCREMENT NOT NULL   |
| name                   | TEXT        | NOT NULL                             |
| personalCount          | INTEGER     | NOT NULL                             |
| usePersonalDescription | INTEGER     | NOT NULL DEFAULT 0                   |

```
CREATE TABLE IF NOT EXISTS Album (uid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, personalCount INTEGER NOT NULL, usePersonalDescription Integer NOT NULL DEFAULT 0)
```

## Role
| Column      | Type        | Options            |
| :---------- | ----------- | ------------------ |
| username    | TEXT        | NOT NULL UNIQUE    |
| albumuid    | INTEGER     | NOT NULL           |
| role        | INTEGER     | NOT NULL DEFAULT 0 |

```
CREATE TABLE IF NOT EXISTS Role (username TEXT UNIQUE NOT NULL, albumuid INTEGER NOT NULL, role INTEGER NOT NULL DEFAULT 0)
```

## Pictures
| Column      | Type     | Options           |
| :---------- | -------- | ----------------- |
| filename    | TEXT     | NOT NULL UNIQUE   |
| owner       | TEXT     | NOT NULL          |
| albumuid    | INTEGER  | NOT NULL          |
| foldertype  | INTEGER  | NOT NULL          |
| priority    | INTEGER  | NOT NULL          |
| description | TEXT     | |

```
CREATE TABLE IF NOT EXISTS Pictures (filename TEXT UNIQUE NOT NULL, owner TEXT NOT NULL, albumid INTEGER NOT NULL, foldertype INTEGER NOT NULL, priority INTEGER NOT NULL, description TEXT)
```

## AccessToken
| Column      | Type    | Options           |
| :---------- | ------- | ----------------- |
| username    | TEXT    | NOT NULL UNIQUE   |
| accesstoken | TEXT    | NOT NULL UNIQUE   |

```
CREATE TABLE IF NOT EXISTS AccessToken (username TEXT UNIQUE NOT NULL, accesstoken TEXT UNIQUE NOT NULL)
```