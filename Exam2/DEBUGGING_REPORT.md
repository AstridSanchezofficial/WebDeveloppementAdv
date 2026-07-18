# Debugging Report

## BUG 1: App was not connected with the data base

- Original Code :db = SQLAlchemy
-  **Description:** The SQLAlchemy instance was not initialized with the Flask application, preventing the application from connecting to and interacting with the database.

- Code after Fixing: db = SQLAlchemy(app)


## BUG 2 :
