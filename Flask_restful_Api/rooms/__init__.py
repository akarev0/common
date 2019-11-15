from flask import Blueprint
from flask_restful import Api

from rooms.rooms import RoomsChange


rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)


api.add_resource(RoomsChange, '/rooms', '/rooms/<value>')
