
# API definitation
## URI
| URI         | Description | Method      | Parameters  | Response Code | Response |
| :---------- | ----------- | ----------- | ----------- | ------------- | -------- |
| /api/login.php | send login request | POST | username - String <br> password - String | 200 OK <br/> 400 Bad Request | 200 Access Token <br> 400 Fail message |
| /api/register.php | send register request | POST | username - String <br> password - String <br> nickname - String <br> email - String | 200 OK <br> 400 Bad Request | 200 Access Token <br> 400 Fail message |
| /api/create.php | create new album | POST | albumname - String <br> personalpicturecount - int <br> usepersonaldescription - Boolean <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized  | 200 Album uid <br> 400 Fail message <br> 401 None |
| /api/setrole.php | set role(Only admin) | POST | albumname - String <br> username - String <br> role - RoleType <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None |
| /api/getrole.php | get role | POST | albumname - String <br> username - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 RoleType <br> 400 Fail message <br> 401 None |
| /api/addpicture.php | add new picture | POST | albumname - String <br> foldertype - FolderType <br> picture - File <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None |
| /api/setpersonalpicturecount.php | set personal picture count | POST | albumname - String <br> count - int <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None |
| /api/setpersonaldescriptionuse.php | set personal description use flag | POST | albumname - String <br> flag - Boolean <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None |
| /api/getpicturelist.php | get picture list | POST | albumname - String <br> foldertype - FolderType <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 picture path list (Type : JSON) <br> 400 Fail message <br> 401 None |
| /api/getpictureinfo.php | get picture | POST | albumname - String <br> foldertype - FolderType <br> picturepath - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 picture info (Type : JSON) <br> 400 Fail message <br> 401 None |
| /api/setdescription.php | set description | POST | albumname - String <br> foldertype - FolderType <br> description - String <br> accesstoken - String | 200 OK <br> 400 Bad Request <br> 401 Unauthorized | 200 None <br> 400 Fail message <br> 401 None |
| /api/getalbumlist.php | get album list | POST | None | 200 OK <br> 404 Not Found | 200 album list info (Type : JSON) <br> 404 Server error.. |


## Examples
### /api/getpicturelist.php
#### Input
```
albumname=blablabla&foldertype=0&accesstoken=
```
#### Output
```
{"}
```