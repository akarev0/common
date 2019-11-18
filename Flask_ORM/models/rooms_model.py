from db import db


class RoomsModel(db.Model):
    __tablename__ = "rooms"

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String, unique=False)
    price = db.Column(db.Integer)
    tenant_ID = db.Column(db.Integer)
