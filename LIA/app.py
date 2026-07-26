from flask import (Flask, flash, redirect, render_template, request, url_for)
from models import db,User,Book
from helpers import (validate_username,validate_password,validate_email,flash_errors,find_user,validate_reading_status,reading_status,validate_input,validate_note,find_book)
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

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = find_user(username)

        if user is None or not user.check_password(password):
            flash("Username or password are not valid. Please try again", "error")
            return render_template("login.html", username=username)

        login_user(user)
        flash("You are logged in", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/logout", methods = ["POST"])
@login_required
def logout():
    logout_user()

    flash("You have been logged out", "success")
    return redirect(url_for("home"))

@app.route("/dashboard")
@login_required
def dashboard():
    user_books = current_user.books

    return render_template("books.html", username=current_user.username, books=user_books)
        
@app.route("/book/add", methods = ["POST", "GET"])
def add_book():
    if request.method == "POST":
        user_id = current_user.id

        title = request.form["title"].strip().title()
        author = request.form["author"].strip().title()
        note = request.form["note"].strip()
        status = request.form["status"]
        errors = []

        title_errors = validate_input(title, "title")
        author_errors = validate_input(author, "author")
        note_error = validate_note(note)
        status_error = validate_reading_status(status)
        
        validation = [title_errors, author_errors, note_error, status_error]

        for result in validation:
            if result:
                errors.append(result)
        
        if errors:
            flash_errors(errors)
            
            return render_template("book_form.html", title=title, author=author, note=note, status=status, status_options=reading_status)
        
    
        book = Book(title=title, author=author, note=note, reading_status=status, user_id=current_user.id)

        db.session.add(book)
        db.session.commit()

        flash(f"You  added {title} to your list.", "success")

        return redirect(url_for("dashboard"))

    return render_template("book_form.html", status_options=reading_status)

@app.route("/book/edit/<int:book_id>", methods = ["POST", "GET"])
def book_edit(book_id):
    user_id = current_user.id
    book = find_book(user_id, book_id)

    if request.method == "POST":
        new_note = request.form["note"]
        new_status = request.form["status"]
        errors = []

        note_error = validate_note(new_note)
        status_error = validate_reading_status(new_status)

        validation = [note_error, status_error]

        for result in validation:
            if result:
                errors.append(result)
        
        if errors:
            flash_errors(errors)
            
            return render_template("edit_book.html", note=new_note, book=book, status_options=reading_status)
        
        book.note = new_note
        book.reading_status = new_status
        db.session.commit()
        flash(f"You have successfully updated {book.title} by {book.author}")
        return redirect(url_for("dashboard"))

    return render_template("edit_book.html", book=book, status_options=reading_status)

@app.route("/book/delete/<int:book_id>", methods=["POST"])
def book_delete(book_id):
    user_id = current_user.id
    book = find_book(user_id, book_id)

    if request.method == "POST":
        flash(f"You have deleted {book.title} by {book.author}")
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for("dashboard"))
