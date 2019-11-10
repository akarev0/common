from flask import Blueprint
from flask_restful import Api

from stuff.stuff import StuffChange

api_bp = Blueprint('stuff', __name__)
api = Api(api_bp)


api.add_resource(StuffChange, '/stuff', '/stuff/<value>')
