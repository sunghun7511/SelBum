#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from datetime import timedelta
import hashlib, sqlite3, re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



app = Flask(__name__)
app.secret_key = "Code_Review_Fuck_you_HAAHAHAHAAHAHHAHAHAHAHAHAHAHHAHAHAHAHAAH"

@app.route("/")
@app.route("/index.html")
@app.route("/landing.html")
def index():
    username = getUsername()
    names = dict()
    my = dict()
    if username != None:
        re = queryDB("SELECT albumuid FROM Role WHERE username=? AND role=0", [username])
        for r in re:
            names[r] = queryDB("SELECT name FROM Album WHERE uid=?", [r])[0][0]
        re2 = queryDB("SELECT albumuid FROM Role WHERE username=? AND role=1", [username])
        for r2 in re2:
            my[r] = queryDB("SELECT name FROM Album WHERE uid=?", [r])[0][0]

    return render_template("landing.html", s_username = username, s_nickname = getNickname(username), my = my, names = names)

@app.route("/auth.html")
def auth():
    return render_template("auth.html")

@app.route("/album.html", methods=["GET"])
def album():
    username = getUsername()
    if username == None:
        return build()
    aid = request.args.get("albumid")

    return render_template("album.html", s_username = username, s_nickname = getNickname(username))

@app.route("/logout")
def auth_logout():
    if isLogin():
        session.pop("username", None)
        return build("로그아웃 하였습니다.")
    else:
        return build("로그인되지 않았습니다.")

@app.route("/login", methods=["POST"])
def auth_login():
    id = request.form["loginId"].strip()
    pw = password_hash(request.form["loginPw"].strip())

    if len(id) < 5 or len(id) > 30:
        return back("아이디가 너무 짧거나 깁니다.")
    
    res = queryDB("SELECT nickname FROM User WHERE username=? AND phash=?", [id, pw])
    
    if len(res) == 0:
        return back("아이디 또는 비밀번호를 데이터베이스에서 검색을 하다가 보여줄 결과물을 찾지 못해서 이런 결과를 내보내게 되었습니다. 이 결과에 대해 대단히 죄송하게 생각하는 바입니다.")
    
    session['username'] = id

    return str(unicode("<script>alert(\"로그인하였습니다!\\n"+res[0][0]+" 님\");location.href=\"/\"</script>"))

@app.route("/register", methods=["POST"])
def auth_register():
    username = request.form["signupId"].strip()
    password = request.form["signupPw"].strip()
    nickname = request.form["signupNickname"].strip()
    email = request.form["signupEmail"].strip()

        
    if username == None or username == "":
        return back("아이디는 공백일 수 없습니다.")
    
    if len(username) < 4 or len(username) > 20:
        return back("아이디는 4글자 ~ 20글자 사이로 입력해주세요.")
    
    m = re.search("[a-zA-Z0-9\\*\\$\\_\\&\\!]+", username)
    if m is None or len(m.group()) != len(username):
        return back("아이디가 올바르지 않습니다!")
    
    dbres = queryDB("SELECT * FROM User WHERE username=?", [username])
    if dbres is not None and len(dbres) != 0:
        return back("이미 존재하는 아이디입니다!")
    
    
    if password == None or password == "":
        return back("비밀번호는 공백일 수 없습니다.")
    
    if len(password) < 6 or len(password) > 20:
        return back("비밀번호는 6글자 ~ 20글자 사이로 입력해주세요.")
    
    if password == username:
        return back("아이디와 비밀번호는 같을 수 없습니다!")
    
    m = re.search("[a-zA-Z0-9@\\*\\$\\_\\&\\!]+", password)
    if m is None or len(m.group()) != len(password):
        return back("비밀번호가 올바르지 않습니다!")
    
    
    if email is None or len(email) < 3:
        return back("올바르지 않은 이메일입니다!")
    
    m = re.search("([\.0-9a-z_-]+)@([0-9a-z_-]+)(\.[0-9a-z_-]+){1,2}", email)
    if m is None or len(m.group()) != len(email):
        return back("올바르지 않은 이메일입니다!")
    
    dbres = queryDB("SELECT * FROM User WHERE email=?", [email])
    if dbres is not None and len(dbres) != 0:
        return back("이미 존재하는 이메일입니다!")
    
    
    
    if nickname == None or nickname == "":
        nickname = username
    
    if len(nickname) < 1 or len(nickname) > 20:
        return back("닉네임은 1글자 ~ 20글자 사이로 입력해주세요.")
    
    m = re.search("[a-zA-Z0-9\\*\\$\\_\\&\\!가-힣　 ]+", nickname)
    if m is None or len(m.group()) != len(nickname):
        return back("닉네임이 올바르지 않습니다!")
    
    m = re.search("[ ]+", nickname)
    if m is not None and len(m.group()) == len(nickname):
        return back("닉네임이 올바르지 않습니다!")
    
    dbres = queryDB("SELECT * FROM User WHERE nickname=?", [nickname])
    if dbres is not None and len(dbres) != 0:
        return back("이미 존재하는 닉네임입니다!")

    phash = password_hash(password)
    queryDB("INSERT INTO User (username, nickname, phash, email) VALUES(?, ?, ?, ?);", [username, nickname, phash, email])

    return str(unicode("<script>alert(\"회원가입 하였습니다.\\n"+nickname+" 님\");location.href=\"/\"</script>"))



def getUsername():
    if isLogin():
        return session["username"]
    else:
        return None


def getNickname(username):
    q = queryDB("SELECT nickname FROM User WHERE username=?", [username])
    if q is None or len(q) == 0:
        return None
    return q[0][0]

def isLogin():
    return "username" in session and session["username"] != ""

def build(message="로그인이 필요합니다.", to="index.html"):
    if not to.startswith("/"):
        to = "/" + to
    return str(unicode("<script>alert(\"" + message + "\");location.href=\"" + to + "\";</script>"))

def back(message="로그인이 필요합니다."):
    return str(unicode("<script>alert(\"" + message + "\");window.history.back();</script>"))

def password_hash(password):
    h = hashlib.sha512()
    h.update(str(password).encode('utf-8'))
    return str(h.hexdigest())

DATABASE = 'database.db'

def initDB():
#    queryDB("DROP TABLE IF EXISTS User")
    res = str(queryDB("CREATE TABLE IF NOT EXISTS User (username TEXT PRIMARY KEY NOT NULL, nickname TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, phash TEXT NOT NULL)"))

#    queryDB("DROP TABLE IF EXISTS Album")
    res += "\n\n" + str(queryDB("CREATE TABLE IF NOT EXISTS Album (uid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, personalCount INTEGER NOT NULL, usePersonalDescription Integer NOT NULL DEFAULT 0)"))
    
    
#    queryDB("DROP TABLE IF EXISTS Role")
    res += "\n\n" + str(queryDB("CREATE TABLE IF NOT EXISTS Role (username TEXT UNIQUE NOT NULL, albumuid INTEGER NOT NULL, role INTEGER NOT NULL DEFAULT 0)"))
    
    
#    queryDB("DROP TABLE IF EXISTS Pictures")
    res += "\n\n" + str(queryDB("CREATE TABLE IF NOT EXISTS Pictures (filename TEXT UNIQUE NOT NULL, owner TEXT NOT NULL, albumid INTEGER NOT NULL, foldertype INTEGER NOT NULL, priority INTEGER NOT NULL, description TEXT)"))
    
    
#    queryDB("DROP TABLE IF EXISTS AccessToken")
    res += "\n\n" + str(queryDB("CREATE TABLE IF NOT EXISTS AccessToken (username TEXT UNIQUE NOT NULL, accesstoken TEXT UNIQUE NOT NULL)"))
    
    print("DB connect success")
    return res

def closeDB():
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def getDB():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        print("Connect DB!")
    return db

def queryDB(query, args=(), one=False):
    con = getDB()
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    con.commit()
    return (rv[0] if rv else None) if one else rv



@app.before_first_request
def load():
    initDB()

@app.before_request
def session_timeout():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@app.teardown_appcontext
def close_connection(exception):
    closeDB()

if __name__ == "__main__":
    app.run(debug=True, port=8080)