from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cosplay")
def cosplay():
    return render_template("cosplay.html")

@app.route("/mukbang")
def mukbang():
    return render_template("mukbang.html")
