import json

from flask import request, Response
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

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
        try:
            new_tenant = TenantsModel(**data)
            db.session.add(new_tenant)
            db.session.commit()
            return Response("Tenant {} successfully added".format(data), 200)
        except IntegrityError:
            return Response("This tenant is already exist", 412)

    def put(self, value):
        data = json.loads(request.data)
        if data:
            post = TenantsModel.query.get(value)
            post.age = data.get('age') or post.age
            post.sex = data.get('sex') or post.sex
            post.city = data.get('city') or post.city
            post.address = data.get('address') or post.address
            db.session.commit()
            return Response("Tenant {} successfully update".format(data), 200)

    def delete(self, value):
        post = TenantsModel.query.get(value)
        try:
            db.session.delete(post)
            db.session.commit()
            return Response("Tenant {} successfully fired".format(post.name), 200)
        except UnmappedInstanceError:
            return Response("This tenant didn't live here", 404)
