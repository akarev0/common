from flask_restful import Resource, marshal_with

from books import Books
from library.parser import library_parser
from library.structure import library_structure
from models.models import User


class LibraryView(Resource):

    @marshal_with(library_structure)
    def get(self):
        """method return user books http://127.0.0.1:5000/library?name=<user_name>"""
        args = library_parser.parse_args(strict=True)
        user = User.query.filter_by(name=args.get('name')).first()
        return user.books
