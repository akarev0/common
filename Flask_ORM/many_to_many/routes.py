from flask import request
from flask_restful import Resource, marshal_with, reqparse
import json
from db import db

from models.models import StaffModel, RoomsModel
from rooms.rooms_structure import rooms_structure
from staff.staff_structure import staff_structure


staff_room_parser = reqparse.RequestParser()
staff_room_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")


class StaffView(Resource):
    @marshal_with(staff_structure)
    def get(self):
        return StaffModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_staff = StaffModel(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Successfully added"


class RoomView(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        return RoomsModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_staff = StaffModel(**data)
        db.session.add(new_staff)
        db.session.commit()
        return "Successfully added"


class StaffRoom(Resource):
    @marshal_with(rooms_structure)
    def get(self):
        args = staff_room_parser.parse_args(strict=True)
        staff = StaffModel.query.filter_by(name=args.get('name')).first()
        return staff.room

    def post(self):
        data = json.loads(request.data)
        staff_name = data.get('staff_name')
        room_number = data.get('room_number')
        staff = StaffModel.query.filter_by(name=staff_name).first()
        room = RoomsModel.query.filter_by(number=room_number).first()
        staff.rooms.append(room)
        db.session.commit()
        return "Successfully added {} to {}".format(staff, room)
