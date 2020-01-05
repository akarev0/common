import json

from flask import request, Response
from flask_restful import Resource, marshal_with

from books import Books
from models.models import User, Book
from users.parser import user_book_parser
from users.structure import users_structure, book_structure
from db import db


class Users(Resource):
    @marshal_with(users_structure)
    def get(self, user_id=None):
        if user_id:
            return User.query.get(user_id)
        return User.query.all()

    def post(self):
        data = json.loads(request.data)
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return Response("{} added to User list!".format(data), 200)


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
