from flask_restful import Resource, marshal_with

from models.staff_model import StaffModel
from staff.staff_structure import staff_structure


class Staff(Resource):
    @marshal_with(staff_structure)
    def get(self):
        return StaffModel.query.all()
