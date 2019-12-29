import json

from flask import request, Response, jsonify
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm.exc import UnmappedInstanceError

from db import db
from models.models import StaffModel
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
            return Response("{} was successfully added to staff".format(data), 200)
        except (IntegrityError, DataError):
            return Response("Nobody added, please try change type or make fields unique", 400)

    def put(self, value):
        data = json.loads(request.data)
        post = StaffModel.query.get(value)
        if post:
                post.passport_ID = data.get('passport_ID') or post.passport_ID
                post.name = data.get('name') or post.name
                post.position = data.get('position') or post.position
                try:
                    post.salary = float(data.get('salary')) or post.salary
                    db.session.commit()
                except (ValueError, TypeError):
                    return Response("Salary must be a float type", 400)
        return Response("Staff {} successfully update".format(data), 200)

    def delete(self, value):
        try:
            post = StaffModel.query.get(value)
            db.session.delete(post)
            db.session.commit()
            return Response("Staff {} was successfully fired".format(post.name), 200)
        except UnmappedInstanceError:
            return Response("Staff, passport_ID: {} didn't work here :(".format(value), 400)
