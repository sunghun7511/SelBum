from flask import *

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
@app.route("/landing.html")
def index():
    return render_template("landing.html")

@app.route("/auth.html")
def auth():
    return render_template("auth.html")
app.run(debug=True, port=8080)