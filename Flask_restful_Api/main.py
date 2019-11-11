from flask import Flask, current_app

from config import necessary_config
from rooms import rooms_bp
from stuff import stuff_bp

app = Flask(__name__)

app.config.from_object(necessary_config())


app.register_blueprint(stuff_bp)
app.register_blueprint(rooms_bp)


@app.route('/')
def home_page():
    return current_app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
