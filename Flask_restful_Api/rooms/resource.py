from main import db

class RoomsModel(db.Model):
    __tablename__ = "rooms_table"

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    tenants_id = db.Column(db.Integer, unique=True, nullable=False)
