from flask_restful import fields
from flask_restful.fields import Nested

room_structure = {
    'number': fields.Integer
}

staff_structure = {
    'name': fields.String,
    'rooms': Nested(room_structure)
}
