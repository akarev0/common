from db import db


class StaffModel(db.Model):
    __tablename__ = "staff"

    passport_ID = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    position = db.Column(db.String, unique=True, nullable=True)
    salary = db.Column(db.Integer, unique=False, nullable=True)
