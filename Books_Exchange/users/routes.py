import json

from flask import request, Response
from flask_restful import Resource, marshal_with

from db import db
from models.models import User
from users.structure import users_structure


class Users(Resource):
    @marshal_with(users_structure)
    def get(self, user_id=None):
        if user_id:
            return User.query.get(user_id)
        return User.query.all()

    def post(self):
        data = json.loads(request.data)
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return Response("{} added to User list!".format(data), 200)
