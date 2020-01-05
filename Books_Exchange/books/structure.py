from flask_restful import fields

book_structure = {
    'author': fields.String,
    'book_title': fields.String,
    'edition': fields.String,
    'edition_year': fields.String,
    'translation': fields.String
}
