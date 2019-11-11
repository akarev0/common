from flask import Blueprint
from flask_restful import Api

from stuff.stuff import StuffChange

stuff_bp = Blueprint('stuff', __name__)
api = Api(stuff_bp)


api.add_resource(StuffChange, '/stuff', '/stuff/<value>')
