import json

from flask import request
from flask_restful import Resource, marshal_with, reqparse

from rooms.resource import rooms
from rooms.structure import rooms_structure

parser = reqparse.RequestParser()
parser.add_argument("filter")


class RoomsChange(Resource):
    @marshal_with(rooms_structure)
    def get(self, value=None):
        args = parser.parse_args()
        rooms_filter = []
        if value:
            if args.get('filter'):
                for room in rooms:
                    if room.status == args.get('filter'):
                        rooms_filter.append(room)
                return rooms_filter
            else:
                for room in rooms:
                    if room.number == value:
                        return room
        else:
            return rooms

    def patch(self, value):
        data = request.args
        data_dict = {data.get('key'): data.get('value')}

        for room in rooms:
            print(setattr(room, data['key'], data['value']))
            if room.number == value:
                if data.get('key') == "level":
                    room.level = data.get('value')
                if data.get('key') == "status":
                    room.status = data.get('value')
                if data.get('key') == "price":
                    room.price = data.get('value')
        return "Successfully updated"

    def post(self):
        data = json.loads(request.data)
        rooms.append(data)
        return "New room was successfully add"

    def delete(self, value):
        [rooms.remove(room) for room in rooms if room.number == value]
        return "Room {} was deleted".format(value)
