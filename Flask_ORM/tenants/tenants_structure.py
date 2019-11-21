from flask_restful import fields

address_structure = {
    "city": fields.String,
    "street": fields.String
}

tenants_structure = {
    "passport_ID": fields.String,
    "name": fields.String,
    "age":  fields.Integer,
    "sex": fields.String,
    "address": fields.Nested(address_structure)
}
