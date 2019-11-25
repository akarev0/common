from flask import request
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
                person.salary = data.get('salary') or person.salary
                break

    def delete(self, person_name):
        [staff.remove(person) for person in staff if person.name == person_name]

