import json

from db import db
from flask import request
from flask_restful import Resource, marshal_with

from models.staff_model import StaffModel
from staff.staff_structure import staff_structure


class Staff(Resource):
    @marshal_with(staff_structure)
    def get(self, value=None):
        if value:
            return StaffModel.query.get(value)
        return StaffModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_staff = StaffModel(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Staff {} successfully added".format(new_staff.name)
