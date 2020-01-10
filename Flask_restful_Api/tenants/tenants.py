from flask import request, Response
from flask_restful import Resource, marshal_with

from tenants.resource import tenants
from tenants.structure import tenants_structure


class TenantsChange(Resource):
    @marshal_with(tenants_structure)
    def get(self, tenants_id=None):
        for tenant in tenants:
            if tenant.passport_id == tenants_id:
                return tenant
        return tenants

    def patch(self, tenants_id):
        data = request.args
        for tenant in tenants:
            if tenant.passport_id == tenants_id:
                tenant.name = data.get('name') or tenant.name
                tenant.age = data.get('age') or tenant.age
                tenant.sex = data.get('sex') or tenant.sex
                tenant.room_number = data.get('room_number') or tenant.room_number
                tenant.address = data.get('address') or tenant.address
                return Response("{} info was updated".format(tenant.name), 200)

    def delete(self, tenants_id):
        if tenants_id in [str(tenant.passport_id) for tenant in tenants]:
            [tenants.remove(tenant) for tenant in tenants if tenant.passport_id == tenants_id]
            return Response("{} was fired!".format(tenants_id), 200)
        else:
            return Response("{} doesnt live here".format(tenants_id), 412)
