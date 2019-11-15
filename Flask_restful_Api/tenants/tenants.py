from flask import request
from flask_restful import Resource, marshal_with

from tenants.resource import tenants
from tenants.structure import tenants_structure


class TenantsChange(Resource):
    @marshal_with(tenants_structure)
    def get(self, value=None):
        for tenant in tenants:
            if tenant.name == value:
                return tenant
        return tenants

    def patch(self, value):
        data = request.args
        for tenant in tenants:
            if tenant.name == value:
                if data.get('key') == "passport_id":
                    tenant.passport_id = data.get('value')
                if data.get('key') == "age":
                    tenant.age = data.get('value')
                if data.get('key') == "age":
                    tenant.age = data.get('value')
                if data.get('key') == "sex":
                    tenant.sex = data.get('value')
                if data.get('key') == "room_address":
                    tenant.room_number = data.get('value')
                if data.get('key') == "address":
                    tenant.address = data.get('value')
        return 'Successfully updated'

    def delete(self, value):
        for tenant in tenants:
            if tenant.name == value:
                tenants.remove(tenant)
        return 'Successfully deleted'
