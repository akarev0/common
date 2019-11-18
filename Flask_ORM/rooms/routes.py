import json

from flask import request
from flask_restful import Resource, marshal_with

from db import db
from models.rooms_model import RoomsModel
from rooms.rooms_structure import rooms_structure


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self, value=None):
        if value:
            data = RoomsModel.query.get(value)
            return data
        return RoomsModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_room = RoomsModel(**data)
        db.session.add(new_room)
        db.session.commit()
        return "Room {} successfully added".format(new_room.number)

    def delete(self, value):
        post = RoomsModel.query.get(value)
        db.session.delete(post)
        db.session.commit()
        return "Room {} successfully deleted".format(post.number)
