from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    pass

app.run(debug=True)