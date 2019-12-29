import json
from json import JSONDecodeError

from flask import request, Response
from flask_restful import Resource, marshal_with, reqparse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

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

    def post(self):
        data = json.loads(request.data)
        try:
            new_room = RoomsModel(**data)
            try:
                int(data.get('price'))
            except ValueError:
                return Response("Price must be integer!", 412)
            if int(data.get('price')) < 0:
                return Response("Price cannot be negative!", 412)
            db.session.add(new_room)
            db.session.commit()
            return Response("Room {} successfully added!".format(data), 200)
        except IntegrityError:
            return Response("This room is already exist!", 412)

    def put(self, value):
        data = json.loads(request.data)
        if data:
            post = RoomsModel.query.get(value)
            post.number = data.get('number') or post.number
            post.level = data.get('level') or post.level
            post.status = data.get('status') or post.status
            post.price = data.get('price') or post.price
            post.tenant_ID = data.get('tenant_ID') or post.tenant_ID
            db.session.commit()
            return Response("Room {} successfully update".format(data), 200)

    def delete(self, value):
        post = RoomsModel.query.get(value)
        try:
            db.session.delete(post)
            db.session.commit()
            return Response("Room {} successfully deleted".format(post.number), 200)
        except UnmappedInstanceError:
            return Response("This room did not exist!", 404)
