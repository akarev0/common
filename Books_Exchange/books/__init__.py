from flask import Blueprint
from flask_restful import Api

from books.routes import Books

books_bp = Blueprint('books', __name__)
api_books = Api(books_bp)


api_books.add_resource(Books, '/books', '/books/<name>')
