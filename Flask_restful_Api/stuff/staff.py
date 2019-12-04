from flask import request, Response
from flask_restful import Resource, marshal_with

from stuff.resource import staff
from stuff.structure import staff_structure


class StaffChange(Resource):
    @marshal_with(staff_structure)
    def get(self, person_name=None):
        for person in staff:
            if person.name == person_name:
                return person
        return staff

    def patch(self, person_name):
        data = request.args
        for person in staff:
            if person.name == person_name:
                person.passport_id = data.get('passport_id') or person.passport_id
                person.position = data.get('position') or person.position
                if data.get('salary'):
                    try:
                        person.salary = float(data.get('salary')) or person.salary
                    except ValueError:
                        return Response("Wrong type", 400)
                return Response("Person {} updated".format(person_name), 200)

    def delete(self, person_name):
        if person_name in [str(person.name) for person in staff]:
            [staff.remove(person) for person in staff if person.name == person_name]
            return Response("{} was fired!".format(person_name), 200)
        else:
            return Response("{} doesnt work here".format(person_name), 412)
