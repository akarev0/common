from flask import Flask
from flask_migrate import Migrate

from config import run_config
from create_db import create_db
from db import db
from many_to_many import staff_room
from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(rooms_bp)
    app.register_blueprint(tenants_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(create_db)
    app.register_blueprint(staff_room)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
