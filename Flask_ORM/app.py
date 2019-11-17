from flask import Flask

from config import run_config
from db import db
from rooms import rooms_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())
    db.init_app(app)
    app.register_blueprint(rooms_bp)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
