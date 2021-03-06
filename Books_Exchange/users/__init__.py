from flask import Blueprint
from flask_restful import Api

from users.routes import Users

users_bp = Blueprint('users', __name__)
api_users = Api(users_bp)


api_users.add_resource(Users, '/users', '/users/<user_id>')

