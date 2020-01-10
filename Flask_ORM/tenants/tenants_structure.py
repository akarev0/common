from flask_restful import fields


tenants_structure = {
    "passport_ID": fields.String,
    "name": fields.String,
    "age":  fields.Integer,
    "sex": fields.String,
    "city": fields.String,
    "address": fields.String
}
