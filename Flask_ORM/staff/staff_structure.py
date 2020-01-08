from flask_restful import fields

staff_structure = {
    "passport_ID": fields.String,
    "name": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}
