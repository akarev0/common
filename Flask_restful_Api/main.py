from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

from config import necessary_config
from rooms import rooms_bp
from stuff import staff_bp
from tenants import tenants_bp

app = Flask(__name__)

app.config.from_object(necessary_config())
db = SQLAlchemy(app)

app.register_blueprint(staff_bp)
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)


@app.route('/')
def home_page():
    return current_app.config['SECRET_KEY']


if __name__ == '__main__':
    app.run(debug=True)
