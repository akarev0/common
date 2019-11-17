from flask_restful import Resource, marshal_with

from models.rooms_model import Rooms
from rooms import rooms_structure


class Room(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        return Rooms
