# Debugging Report

## BUG 1: App was not connected with the data base

- Original Code :db = SQLAlchemy
-  **Description:** The SQLAlchemy instance was not initialized with the Flask application, preventing the application from connecting to and interacting with the database.

- Code after Fixing: db = SQLAlchemy(app)


## BUG 2 : Fixed invalid configuration

- Original Code: app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///albums.db"
- Code after Fixing : app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"

- Original code:with app.app_context:
- Code after fixing:  with app.app_context():
                             db.create_all()

- Description :Called app.app_context() to properly initialize the application context and removed the invalid SQLALCHEMY_DATABASE_URL configuration, keeping only SQLALCHEMY_DATABASE_URI.
