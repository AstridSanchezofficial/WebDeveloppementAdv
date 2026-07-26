from flask import (Flask, flash, redirect, render_template, request, url_for)
from models import db,User,Book
from helpers import (validate_username,validate_password,validate_email,flash_errors)
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

@app.route("/register", methods=["GET","POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method=="POST":
        username=request.form["username"].strip()
        email=request.form["email"].lower().strip()
        password=request.form["password"]
        errors=[]

        username_errors=validate_username(username)
        email_errors=validate_email(email)
        password_errors=validate_password(password)

        validations=[password_errors,email_errors,username_errors]

        for error in validations:
            if error:
                errors.extend(error)
        if errors:
            flash_errors(errors)
            return render_template("register.html", username=username)

        user=User(username=username,email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Your account was created", "success")
        return redirect(url_for('login'))


    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("dashboard.html")

