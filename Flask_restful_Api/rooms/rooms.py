import json

from flask import request
from flask_restful import Resource, marshal_with, reqparse

from rooms.resource import rooms, Rooms
from rooms.structure import rooms_structure

parser = reqparse.RequestParser()
parser.add_argument("filter")


class RoomsChange(Resource):
    @marshal_with(rooms_structure)
    def get(self, room_number=None):
        args = parser.parse_args()
        rooms_filter = []
        if room_number:
            for room in rooms:
                if room.number == room_number:
                    return room
        else:
            if args.get('filter'):
                for room in rooms:
                    if room.status == args.get('filter'):
                        rooms_filter.append(room)
                return rooms_filter
            return rooms

    def patch(self, room_number):
        data = request.args
        for room in rooms:
            if room.number == room_number:
                room.level = data.get('level') or room.level
                room.status = data.get('status') or room.status
                room.price = data.get('price') or room.price
                break

    def post(self):
        data = json.loads(request.data)
        if str(data.get('number')) in [str(room.number) for room in rooms]:
            raise ValueError("This room is already exist")
        if data.get('price') >= 0:
            new_room = Rooms(data.get('number'), data.get('level'), data.get('status'), data.get('price'))
            rooms.append(new_room)
            return "append"
        raise ValueError("Price cant be negative")

    def delete(self, room_number):
        [rooms.remove(room) for room in rooms if str(room.number) == room_number]
