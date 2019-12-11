from flask import Blueprint
from flask_restful import Api

from stuff.staff import StaffChange

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)


api.add_resource(StaffChange, '/staff', '/staff/<person_name>')
