from models import db,User,Book
from flask import flash

def find_user(username):
    return User.query.filter_by(username=username).first()


def validate_username (username):
    user_error=[]

    if not username:
        user_error.append("Username cannot be empty")

    if len(username)>20:
        user_error.append("Username cannot be greater than 20 ")
    if any(character.isspace() for character in username):
        user_error.append("Usernames cannot contain a white space")

    user_exists=find_user(username)

    if user_exists:
        user_error.append("Username already exists, please choose another username")

    if not user_error:
        return None

    return user_error
def validate_password(password):
    password_error=[]

    if len(password)< 8:
        password_error.append("Your password needs to have minimun 8 characters")

    if len(password)>20:
        password_error.append("Password cannot have more than 20 characters")

    if not any(character.isupper() for character in password)or \
        not any(character.isdigit() for character in password ):
        password_error.append("Password needs to have at least an uppercase and a digit character")

    if not password_error:
        return None
    return password_error

# EMAIL VALIDATION
def find_email(email):
    return User.query.filter_by(email=email).first()
def validate_email(email):
    email_error=[]
    if len(email) > 80:
        email_error.append("Email cannot have more than 80 characters")
    if not("@" and "." in email):
        email_error.append("Enter a valid email address")

    email_exist=find_email(email)    

    if email_exist:
        email_error.append("This address is already used. Enter a different one")

    if not email_error:
        return None

    return email_error
    
def flash_errors(errors):
    for error_msg in errors:
        flash(error_msg, "error")
        print(error_msg)


# BOOK VALIDATION
def find_book(user_id, book_id):
    return Book.query.filter_by(user_id=user_id, id=book_id).one_or_404(description=f"No book with the id '{book_id}'.")
def validate_input(input, inputType):
    input_errors = []

    if not input:
        input_errors.append(f"{inputType.capitalize()} is a required field")
    
    if len(input) > 100:
        input_errors.append(f"{inputType.capitalize()} cannot be longer than 100 characters")
    
    if not input_errors:
        return None
    
    return input_errors

def validate_note(note):
    if len(note) > 1000:
        return [f"Your note cannot be longer than 1000 characters"]
    
    return None


reading_status = [
    "Want to read",
    "Reading",
    "Finished"
]

def validate_reading_status(status):
    if not status in reading_status:
        return ["Reading status must be an option from the selection menu"]
    
    return None

def flash_errors(errors):
    for error in errors:
        for error_msg in error:
            flash(error_msg, "error")
            print(error_msg)