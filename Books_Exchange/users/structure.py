from flask_restful import fields

users_structure = {
    'name': fields.String,
    'email': fields.String,
    'library': fields.String
}
