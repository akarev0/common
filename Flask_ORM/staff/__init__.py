from flask import Blueprint
from flask_restful import Api

from staff.routes import Staff

staff_bp = Blueprint('staff', __name__)
api_staff = Api(staff_bp)

api_staff.add_resource(Staff, '/staff', '/staff/<value>')
