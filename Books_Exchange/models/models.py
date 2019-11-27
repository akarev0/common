from db import db


class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    library = db.Column(db.String, nullable=False)


class Book(db.Model):
    author = db.Column(db.String, nullable=False)
    name = db.Column(db.String, primary_key=True)
    edition = db.Column(db.String, nullable=False)
    edition_year = db.Column(db.String, nullable=False)
    translation = db.Column(db.String)


class Library(db.Model):
    pass
