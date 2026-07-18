# Debugging Report

## BUG 1: App was not connected with the data base

- Original Code :db = SQLAlchemy
-  **Description:** The SQLAlchemy instance was not initialized with the Flask application, preventing the application from connecting to and interacting with the database.

- Code after Fixing: db = SQLAlchemy(app)


## BUG 2 : Fixed invalid configuration

- Original Code: app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///albums.db"
- Code after Fixing it : app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///albums.db"

- Original code:with app.app_context:
- Code after fixing it:  with app.app_context():
                             db.create_all()

- Description :Called app.app_context() to properly initialize the application context and removed the invalid SQLALCHEMY_DATABASE_URL configuration, keeping only SQLALCHEMY_DATABASE_URI.

## BUG 3: Incorrect Flask endpoint names in navigation links
- Original Code:   `<a href="{{ url_for('albums') }}"> All Albums </a>`
- Code after Fixing:    ` <a href="{{ url_for('index') }}"> All Albums </a>`

- Original Code:   `<a href="{{ url_for('add') }}"> Add Album </a>`
- Code after Fixing it :  `</a> href="{{ url_for('add_album') }}"> Add Album </a>`

- Description: The navigation menu was using incorrect endpoint names in the url_for() function.

## BUG 4: The album object was not being added to the database
- Original code:```def add_album():
    if request.method == "POST":
        album = Album(
            title=request.form["title"],
            artist=request.form["artist"],
            genre=request.form["genre"],
            year=request.form["year"],
            stock=request.form["stock"]
        )
        db.session.commit()```
- Code after fixing it:```def add_album():
    if request.method == "POST":
        album = Album(
            title=request.form["title"],
            artist=request.form["artist"],
            genre=request.form["genre"],
            year=request.form["year"],
            stock=request.form["stock"]
        )
        db.session.add(album)
        db.session.commit()```
- Description: : The album object was not added to the database session before calling db.session.commit(), so no new album was saved
## BUG 5: fix: correct HTTP method for delete endpoint

- Original code:```@app.route(
    "/albums/<int:album_id>/delete",
    methods=["GET"]```
- Code after fizxing it:```@app.route(
    "/albums/<int:album_id>/delete",
    methods=["POST"]```
- Description:The album deletion route was configured to accept GET requests instead of POST. Since deleting a resource changes application data, the route should only accept POST requests to follow HTTP conventions and prevent unintended deletions.

## BUG 6: Filter albums by   genre instead of artist
- Original code: ```if genre:
    albums = Album.query.filter_by(
        artist=genre
    ).all()
else:
    albums = Album.query.all()```
- Code after fixing it:```if genre:
    albums = Album.query.filter_by(
        genre=genre
    ).all()
else:
    albums = Album.query.all()```
- Description The album filtering logic was using the artist field instead of the genre field when filtering by the selected genre. As a result, the query returned incorrect results because it compared the genre value against the artist column.


