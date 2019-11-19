from flask import Blueprint
from flask_restful import Api

from api.films.recource import FilmsResource

films_bp = Blueprint('films', __name__)
api_films = Api(films_bp)


api_films.add_resource(FilmsResource, '/films')



