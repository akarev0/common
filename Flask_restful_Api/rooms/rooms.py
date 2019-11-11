from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from rooms.resource import rooms


rooms_structure = {
    "number": fields.Integer,
    "level": fields.String,
    "status": fields.String,
    "price": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument("filter")


class RoomsChange(Resource):
    @marshal_with(rooms_structure)
    def get(self, value):
        args = parser.parse_args()
        print(args)
        for room in rooms:
            if room.number == value:
                return room
        return rooms

    def patch(self, value):
        data = request.args
        for room in rooms:
            if room.number == value:
                if data.get('key') == "level":
                    room.level = data.get('value')
                if data.get('key') == "status":
                    room.status = data.get('value')
                if data.get('key') == "price":
                    room.price = data.get('value')
        return "updated"

    def delete(self, value):
        for room in rooms:
            if room.number == value:
                rooms.remove(room)
        return "Room {} was deleted".format(value)

