from flask import Flask, current_app
from flask_restful import Api

from config import necessary_config
from stuff.stuff import StuffChange

app = Flask(__name__)
api = Api(app)
app.config.from_object(necessary_config())


api.add_resource(StuffChange, '/stuff', '/stuff/<value>')


@app.route('/')
def home_page():
    return current_app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
