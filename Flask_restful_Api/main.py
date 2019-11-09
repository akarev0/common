import json

from flask import Flask, current_app, request
from flask_restful import Api, Resource
from config import necessary_config
from utils import rooms_info, stuff_info

app = Flask(__name__)
api = Api(app)
app.config.from_object(necessary_config())


class Staff(Resource):
    def get(self, value):
        for person in stuff_info():
            if person.get('name') == value:
                return person
        return stuff_info()

    def patch(self):
        data = json.loads(request.data)

        return 'PATCH'

    def delete(self):
        return 'DELETE'


api.add_resource(Staff, '/stuff', '/stuff/<value>')


@app.route('/')
def home_page():
    return current_app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
