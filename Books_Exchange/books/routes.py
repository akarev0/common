import json

from flask import request
from flask_restful import Resource, marshal_with

from books.structure import book_structure
from models.models import Book
from db import db


class Books(Resource):
    @marshal_with(book_structure)
    def get(self, name=None):
        if name:
            return Book.query.get(name)
        return Book.query.all()

    def post(self):
        data = json.loads(request.data)
        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
