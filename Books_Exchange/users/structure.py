from flask_restful import fields

users_structure = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

book_structure = {
    "name": fields.String
}
