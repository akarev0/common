import json

from flask import request, Response
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
                return Response("{} info was updated".format(room.number), 200)

    def post(self):
        data = json.loads(request.data)
        if str(data.get('number')) in [str(room.number) for room in rooms]:
            return Response("This room is already exist", 412)
        if data.get('price') > 0:
            new_room = Rooms(data.get('number'), data.get('level'), data.get('status'), data.get('price'))
            rooms.append(new_room)
            return Response("Room {} was added".format(data.get('number')), 201)
        return Response("Price cant be negative", 412)

    def delete(self, room_number):
        if room_number in [str(room.number) for room in rooms]:
            [rooms.remove(room) for room in rooms if str(room.number) == room_number]
            return "Room {} was deleted".format(room_number)
        else:
            return Response("This room doesnt exist", 412)
