from flask import request
from flask_restful import Resource, marshal_with

from stuff.resource import staff
from stuff.structure import staff_structure


class StaffChange(Resource):
    @marshal_with(staff_structure)
    def get(self, value=None):
        for person in staff:
            if person.name == value:
                return person
        return staff

    def patch(self, value):
        data = request.args
        for person in staff:
            if person.name == value:
                if data.get('key') == "passport_id":
                    person.passport_id = data.get('value')
                if data.get('key') == "position":
                    person.position = data.get('value')
                if data.get('key') == "salary":
                    person.salary = data.get('value')
        return "updated"

    def delete(self, value):
        for person in staff:
            if person.name == value:
                staff.remove(person)
        return "deleted"
