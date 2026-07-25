from flask import (Flask, flash,redirect,render_template,request,url_for)
# from flask_login import (login_required, current_user, login_user, logout_user, LoginManager)


app=Flask(__name__)

# app.secret_key = "myKey"

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route("/")
def home():
    return render_template("home.html")