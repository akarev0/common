import json

from flask import request
from flask_restful import Resource, marshal_with

from models.models import User
from users.structure import users_structure
from db import db


class Users(Resource):
    @marshal_with(users_structure)
    def get(self, name=None):
        if name:
            return User.query.get(name)
        return User.query.all()

    def post(self):
        data = json.loads(request.data)
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()

