from flask import Flask, current_app

from config import necessary_config
from stuff import api_bp

app = Flask(__name__)

app.config.from_object(necessary_config())


app.register_blueprint(api_bp)


@app.route('/')
def home_page():
    return current_app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
