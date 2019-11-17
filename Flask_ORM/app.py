from flask import Flask

from config import run_config
from create_db import create_db
from db import db
from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)

    app.register_blueprint(rooms_bp)
    app.register_blueprint(tenants_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(create_db)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
