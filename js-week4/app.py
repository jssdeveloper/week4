from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/cities")
def cities():
    return render_template("cities.html")

@app.route("/log")
def log():
    return render_template("log.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return render_template("login.html")