from flask_restful import Resource, fields, marshal_with

from stuff.resource import Stuff

stuff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}


class StuffChange(Resource):
    @marshal_with(stuff_structure)
    def get(self):
        return stuff


stuff = [Stuff("James", "MR229561", "Director", 15000), Stuff("Lars", "MR223561", "Manager", 13000),
         Stuff("Kirk", "MR228745", "Cock", 11000), Stuff("Robert", "MR123561", "Chambermaid", 9000)]
