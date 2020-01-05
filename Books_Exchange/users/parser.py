
from flask_restful import reqparse

user_book_parser = reqparse.RequestParser()
user_book_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")
