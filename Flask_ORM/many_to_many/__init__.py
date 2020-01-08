from flask import Blueprint
from flask_restful import Api

from many_to_many.routes import StaffView, RoomView, StaffRoom

staff_room = Blueprint('Staff_Room', __name__)
api_staff_room = Api(staff_room)


api_staff_room.add_resource(StaffView, '/staff_1')
api_staff_room.add_resource(RoomView, '/room_1')
api_staff_room.add_resource(StaffRoom, '/staff_room')

