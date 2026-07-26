from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import (generate_password_hash,check_password_hash)

db=SQLAlchemy()

class User(db.Model,UserMixin):

    __tablename__="user"

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    username=db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    email=db.Column(
        db.String(80),
        nullable=False,
        unique=True
    )

    password=db.Column(
        db.String(20),
        nullable=False)

    books=db.relationship(
        "Book",
        back_populates="user"
    )
    #Method 1 -Hashing password (En lugar de guardarla tal cual va a crear una version cifrada de la contrasena)
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    #Method 2 When the user log in it will check if the password is the same when they created the account 

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)    

    #Method 3 

    def __repr__(self):
        return (f'<User:{self.username}, id:{self.id}>')

class Book(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    title=db.Column(
        db.String(255),
        nullable=False,
    )

    author=db.Column(
        db.String(100),
        nullable=False
    )

    note=db.Column(
        db.String(1000),
        nullable=True
    )

    reading_status=db.Column(
        db.String(50),
        nullable=False
    )

    user_id=db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    user=db.relationship(
        "User",
        back_populates="books"
    )

    def __repr__(self):
        return f"<{self.user_id} Book- {self.id}:{self.title}>"

