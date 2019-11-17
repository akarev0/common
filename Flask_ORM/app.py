from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from rooms import rooms_bp

app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(rooms_bp)

if __name__ == "__main__":
    app.run(debug=True)
