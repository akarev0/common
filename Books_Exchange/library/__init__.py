from flask import Blueprint
from flask_restful import Api

from library.routes import LibraryView, BookHolderName

library_bp = Blueprint('library', __name__)
library_api = Api(library_bp)


library_api.add_resource(LibraryView, '/library')
library_api.add_resource(BookHolderName, '/library/holder')
