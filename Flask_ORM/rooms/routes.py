from flask_restful import Resource, marshal_with

from models.rooms_model import RoomsModel
from rooms.rooms_structure import rooms_structure


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        return RoomsModel.query.all()
