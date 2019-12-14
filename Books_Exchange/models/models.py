from db import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author = db.Column(db.String, nullable=False)
    book_title = db.Column(db.String, nullable=False, unique=True)
    edition = db.Column(db.String, nullable=False)
    edition_year = db.Column(db.String, nullable=False)
    translation = db.Column(db.String, nullable=True)
    book_owner = db.Column(db.String, db.ForeignKey('users.id'))


class Library(db.Model):
    __tablename__ = "library"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book = db.Column(db.String, db.ForeignKey('books.name'))
