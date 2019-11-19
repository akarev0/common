import json

from flask import request
from flask_restful import Api, Resource, marshal_with
from db import db


from api.films.structures import films_structure
from db import Films


class FilmsResource(Resource):
    @marshal_with(films_structure)
    def get(self):
        return Films.query.all()

    def post(self):
        body = json.loads(request.data)
        film = Films(**body)
        db.session.add(film)
        db.session.commit()
