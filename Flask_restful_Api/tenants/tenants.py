from flask import request
from flask_restful import Resource, marshal_with

from tenants.resource import tenants
from tenants.structure import tenants_structure


class TenantsChange(Resource):
    @marshal_with(tenants_structure)
    def get(self, tenants_name=None):
        for tenant in tenants:
            if tenant.name == tenants_name:
                return tenant
        return tenants

    def patch(self, tenants_name):
        data = request.args
        for tenant in tenants:
            if tenant.name == tenants_name:
                tenant.passport_id = data.get('passport_id') or tenant.passport_id
                tenant.age = data.get('age') or tenant.age
                tenant.sex = data.get('sex') or tenant.sex
                tenant.room_number = data.get('room_number') or tenant.room_number
                tenant.address = data.get('address') or tenant.address
                break

    def delete(self, tenants_name):
        [tenants.remove(tenant) for tenant in tenants if tenant.name == tenants_name]

