from flask import Blueprint
from flask_restful import Api

from stuff.resource import Stuff

api_bp = Blueprint('stuff', __name__)
api = Api(api_bp)


class StuffEdit:

    def get(self):
        return stuff

    def patch(self):
        pass

        return 'PATCH'

    def delete(self):
        return 'DELETE'


stuff = [Stuff("James", "MR229561", "Director", 15000), Stuff("Lars", "MR223561", "Manager", 13000),
         Stuff("Kirk", "MR228745", "Cock", 11000), Stuff("Robert", "MR123561", "Chambermaid", 9000)]


api.add_resource(StuffEdit, '/stuff', '/stuff/<value>')
