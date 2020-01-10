from db import db


staff_rooms = db.Table(
    "staff_rooms",
    db.Column('passport_ID', db.Integer, db.ForeignKey('staff.passport_ID')),
    db.Column('number', db.Integer, db.ForeignKey('rooms.number'))
)


class StaffModel(db.Model):
    __tablename__ = "staff"

    passport_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    position = db.Column(db.String, unique=True, nullable=True)
    salary = db.Column(db.Integer, unique=False, nullable=True)
    rooms = db.relationship('RoomsModel', secondary=staff_rooms, backref=db.backref('rooms'))


class RoomsModel(db.Model):
    __tablename__ = "rooms"

    number = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String, unique=False)
    price = db.Column(db.Integer)
    tenant_ID = db.Column(db.Integer, db.ForeignKey('tenants.passport_ID'))


class TenantsModel(db.Model):
    __tablename__ = "tenants"

    passport_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    city = db.Column(db.String)
    address = db.Column(db.String)
    tenant_room = db.relationship('RoomsModel', backref='room')
