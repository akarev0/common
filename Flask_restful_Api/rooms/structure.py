from flask_restful import fields

rooms_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "status": fields.String,
    "price": fields.Integer
}
