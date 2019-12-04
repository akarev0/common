from flask_restful import fields

city_structure = {
    "city": fields.String,
    "street": fields.String
}

tenants_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "age": fields.Integer,
    "sex": fields.String,
    "room_number": fields.Integer,
    "address": fields.Nested(city_structure)
}
