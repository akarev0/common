from flask import request, Response
from flask_restful import Resource, marshal_with
import json

from db import db
from models.models import User, Book
from user_books.parser import user_book_parser
from user_books.structure import book_structure


class UserBook(Resource):
    @marshal_with(book_structure)
    def get(self):
        args = user_book_parser.parse_args(strict=True)
        user = User.query.filter_by(name=args.get('name')).first()
        return user.books

    def post(self):
        data = json.loads(request.data)
        user_name = data.get('user_name')
        book_title = data.get('book_title')
        user = User.query.filter_by(name=user_name).first()
        book = Book.query.filter_by(book_title=book_title).first()
        user.books.append(book)
        db.session.commit()
        return Response("Book {} added to {} !".format(book_title, user_name), 200)
