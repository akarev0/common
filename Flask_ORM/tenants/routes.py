import json

from flask import request
from flask_restful import Resource, marshal_with

from models.models import TenantsModel
from tenants.tenants_structure import tenants_structure
from db import db


class Tenants(Resource):
    @marshal_with(tenants_structure)
    def get(self, value=None):
        if value:
            return TenantsModel.query.get(value)
        return TenantsModel.query.all()

    def post(self):
        data = json.loads(request.data)
        new_tenant = TenantsModel(**data)
        db.session.add(new_tenant)
        db.session.commit()

        return "Staff {} successfully added".format(new_tenant.name)

    def put(self, value):
        data = json.loads(request.data)
        post = TenantsModel.query.get(value)

        post.age = data.get('age')
        post.sex = data.get('sex')
        post.city = data.get('city')
        post.address = data.get('address')
        db.session.commit()

        return "Staff {} successfully update".format(post.name)

    def delete(self, value):
        post = TenantsModel.query.get(value)
        db.session.delete(post)
        db.session.commit()

        return "Staff {} was successfully fired".format(post.name)
