from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse

from stuff.resource import Stuff

stuff_structure = {
    "name": fields.String,
    "passport_id": fields.String,
    "position": fields.String,
    "salary": fields.Integer
}


class StuffChange(Resource):
    @marshal_with(stuff_structure)
    def get(self, value):
        for person in stuff:
            if person.name == value:
                return person
        return stuff

    def patch(self, value):
        data = request.args
        print(data.get('key'))
        print(data.get('value'))
        for person in stuff:
            if person.name == value:
                if data.get('key') == "passport_id":
                    person.passport_id = data.get('value')
                if data.get('key') == "position":
                    person.position = data.get('value')
                if data.get('key') == "salary":
                    person.salary = data.get('value')
            return "ok"

    def delete(self, value):
        for person in stuff:
            if person.name == value:
                stuff.remove(person)


stuff = [Stuff("James", "MR229561", "Director", 15000), Stuff("Lars", "MR223561", "Manager", 13000),
         Stuff("Kirk", "MR228745", "Cock", 11000), Stuff("Robert", "MR123561", "Chambermaid", 9000)]
