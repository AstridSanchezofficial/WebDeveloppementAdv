#Debugging Report

## BUG 1: App was not connected with the data base
Original Code :db = SQLAlchemy
Code after Fixing: db = SQLAlchemy(app)
Description: The SQLAlchemy instance was not initialized with the Flask application, preventing the application from connecting to and interacting with the database.
