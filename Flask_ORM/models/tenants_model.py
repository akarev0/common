from db import db


class TenantsModel(db.Model):
    __tablename__ = "tenants"

    passport_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)
    sex = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String, unique=True, nullable=False)
    street = db.Column(db.String, unique=True, nullable=False)
