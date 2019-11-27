from flask_restful import fields

book_structure = {
    'author': fields.String,
    'name': fields.String,
    'edition': fields.String,
    'edition_year': fields.String,
    'translation': fields.String

}