from db import db

# user_books = db.Table(
#     'user_books',
#     db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
#     db.Column('book_id', db.Integer, db.ForeignKey('books.id'))
# )
#  secondary=user_books


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    books = db.relationship('Book', backref='books')


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    author = db.Column(db.String, nullable=False)
    book_title = db.Column(db.String, nullable=False, unique=True)
    edition = db.Column(db.String, nullable=False)
    edition_year = db.Column(db.String, nullable=False)
    translation = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
