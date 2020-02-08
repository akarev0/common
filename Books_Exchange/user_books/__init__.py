from flask import Blueprint
from flask_restful import Api


from user_books.routes import UserBook

user_book_bp = Blueprint('user_books', __name__)
api_user_books = Api(user_book_bp)


api_user_books.add_resource(UserBook, '/user_book')
