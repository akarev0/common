from flask import Blueprint
from flask_restful import Api

from tenants.tenants import TenantsChange


tenants_bp = Blueprint('tenants', __name__)
api = Api(tenants_bp)


api.add_resource(TenantsChange, '/tenants', '/tenants/<tenants_id>')
