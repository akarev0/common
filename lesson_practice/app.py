from flask import Flask

from db import db, migrate
from config import get_config


def create_app(env="DEV"):
    app = Flask(__name__)
    app.config.from_object(get_config())
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
