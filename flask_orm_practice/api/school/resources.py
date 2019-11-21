from flask_restful import Resource, request
from db import School


class SchoolResource(Resource):

    def get(self):
        args = request.args
        name = args.get('name')
        if name:
            return School.query.filter_by(name=name).all()
        return School.query.all()

