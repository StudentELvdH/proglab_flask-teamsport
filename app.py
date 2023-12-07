import os

from flask import Flask, session, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/")
def index():
    return "Project 1: TODO - deze stap uitwerken"

@app.route("/twopeople>", methods=["GET"])
def exercise(twopeople):
       
    db.commit()
    return render_template("exercisestwo.html")

@app.route("/threepeople>", methods=["GET"])
def exercise(threepeople):
       
    db.commit()
    return render_template("exercisesthree.html")

@app.route("/fourpeople>", methods=["GET"])
def exercise(fourpeople):
       
    db.commit()
    return render_template("exercisesfour.html")

