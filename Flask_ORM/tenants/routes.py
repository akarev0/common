from flask_restful import Resource, marshal_with

from models.tenants_model import TenantsModel
from tenants import tenants_structure


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self):
        return TenantsModel.query.all()
