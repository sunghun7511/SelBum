#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from datetime import timedelta
import hashlib, sqlite3


app = Flask(__name__)
app.secret_key = "Code_Review_Fuck_you_HAAHAHAHAAHAHHAHAHAHAHAHAHAHHAHAHAHAHAAH"

@app.route("/")
@app.route("/index.html")
@app.route("/landing.html")
def index():
    return render_template("landing.html")

@app.route("/auth.html")
def auth():
    return render_template("auth.html")

@app.route("/login", methods=["POST"])
def auth_req():
    id = request.form["loginId"].strip()
    pw = password_hash(request.form["loginPw"].strip())

    if len(id) < 5 or len(id) > 30 or len(pw) < 5 or len(pw) > 30:
        return back("아이디 또는 비밀번호가 너무 짧거나 깁니다.")
    
    res = queryDB("SELECT nickname FROM User WHERE username=? AND phash=?", [id, pw])
    
    if len(res) == 0:
        return back("아이디 또는 비밀번호를 데이터베이스에서 검색을 하다가 보여줄 결과물을 찾지 못해서 이런 결과를 내보내게 되었습니다. 이 결과에 대해 대단히 죄송하게 생각하는 바입니다.")

    return "<script>alert(\"로그인하신것을 환영합니다.<br>"+res[0][0]+" 님\");location.href=\"/\"</script>"

@app.route("/register", methods=["POST"])
def auth_req():
    id = request.form["loginId"].strip()
    pw = password_hash(request.form["loginPw"].strip())

    if len(id) < 5 or len(id) > 30 or len(pw) < 5 or len(pw) > 30:
        return back("아이디 또는 비밀번호가 너무 짧거나 깁니다.")
    
    res = queryDB("SELECT nickname FROM User WHERE username=? AND phash=?", [id, pw])
    
    if len(res) == 0:
        return back("아이디 또는 비밀번호를 데이터베이스에서 검색을 하다가 보여줄 결과물을 찾지 못해서 이런 결과를 내보내게 되었습니다. 이 결과에 대해 대단히 죄송하게 생각하는 바입니다.")

    return "<script>alert(\"로그인하신것을 환영합니다.<br>"+res[0][0]+" 님\");location.href=\"/\"</script>"



def back(message="로그인이 필요합니다."):
    return "<script>alert(\"" + message + "\");window.history.back();</script>"

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