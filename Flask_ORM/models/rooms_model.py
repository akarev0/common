from app import db


class Rooms(db.Model):
    __tablename__ = "rooms_table"

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    tenant_ID = db.Column(db.Integer, unique=True, nullable=False)
