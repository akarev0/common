from flask import request, Response
from flask_restful import Resource, marshal_with
import json
from db import db
from library.parser import library_parser
from library.structure import library_structure
from models.models import User, Book


class LibraryView(Resource):

    @marshal_with(library_structure)
    def get(self):
        return Book.query.all()

    def post(self):
        data = json.loads(request.data)
        user_name = data.get('user_name')
        book_title = data.get('book_title')
        user = User.query.filter_by(name=user_name).first()
        book = Book.query.filter_by(book_title=book_title).first()
        user.library.append(book)
        db.session.commit()
        return Response("Book {} added to {} !".format(book_title, user_name), 200)


class BookHolderName(Resource):

    @marshal_with(library_structure)
    def get(self):
        args = library_parser.parse_args(strict=True)
        user = User.query.filter_by(name=args.get('name')).first()
        return user.library
