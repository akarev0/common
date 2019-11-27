from flask import Flask
from flask_migrate import Migrate

from books import books_bp
from create_db import create_db
from db import db
from config import run_config
from users import users_bp


def create_app():
    my_app = Flask(__name__)
    my_app.config.from_object(run_config())

    db.init_app(my_app)
    Migrate(my_app, db)
    my_app.register_blueprint(create_db)
    my_app.register_blueprint(users_bp)
    my_app.register_blueprint(books_bp)

    return my_app


if __name__ == "__main__":
    create_app().run()
