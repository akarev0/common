from flask_restful import Resource


class Stuff(Resource):

    def __init__(self, name, passport_id, position, salary):
        self.name = name
        self.passport_id = passport_id
        self.position = position
        self.salary = salary

