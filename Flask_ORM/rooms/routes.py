import json

from flask import request
from flask_restful import Resource, marshal_with, reqparse

from db import db
from models.models import RoomsModel
from rooms.rooms_structure import rooms_structure

parser = reqparse.RequestParser()
parser.add_argument("filter")


class Rooms(Resource):
    @marshal_with(rooms_structure)
    def get(self, value=None):
        rooms_filter = []
        args = parser.parse_args()
        data = RoomsModel.query.all()
        post = RoomsModel.query.get(value)
        if value:
            if args.get('filter'):
                for post in data:
                    if post.status == args.get('filter'):
                        rooms_filter.append(post)
                return rooms_filter
            else:
                return post
        else:
            return data

    def put(self, value):
        data = json.loads(request.data)
        post = RoomsModel.query.get(value)

        post.number = data.get('number')
        post.level = data.get('level')
        post.status = data.get('status')
        post.price = data.get('price')
        post.tenant_ID = data.get('tenant_ID')
        db.session.commit()

        return "Room {} successfully update".format(post.number)

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
