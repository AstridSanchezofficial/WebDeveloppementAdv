from flask import (Flask, flash,redirect,render_template,request,url_for)
from models import db,User,Book
from flask_login import (login_required, current_user, login_user, logout_user, LoginManager)
import os


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=("sqlite:///bookshelf.db")
app.secret_key = "my-key"
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view="login"
login_manager.init_app(app)
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")