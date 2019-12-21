import json

from sqlalchemy.exc import IntegrityError, DataError

from db import db
from flask import request, Response
from flask_restful import Resource, marshal_with

from models.models import StaffModel, RoomsModel

from staff.staff_structure import staff_structure


class Staff(Resource):
    @marshal_with(staff_structure)
    def get(self, value=None):
        if value:
            return StaffModel.query.get(value)
        return StaffModel.query.all()

    def post(self):
        data = json.loads(request.data)
        try:
            new_staff = StaffModel(**data)
            db.session.add(new_staff)
            db.session.commit()
            return Response("{} was successfully added to staff".format(new_staff.name), 200)
        except (IntegrityError, DataError):
            return Response("Nobody added, please try change type or make fields unique", 400)

    def put(self, value):
        data = json.loads(request.data)
        post = StaffModel.query.get(value)

        post.passport_ID = data.get('passport_ID')
        post.name = data.get('name')
        post.position = data.get('position')
        post.salary = data.get('salary')
        db.session.commit()
        return "Staff {} successfully update".format(post.name)

    def delete(self, value):
        post = StaffModel.query.get(value)
        db.session.delete(post)
        db.session.commit()
        return "Staff {} was successfully fired".format(post.name)


