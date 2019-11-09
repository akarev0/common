import json


def rooms_info():
    with open('rooms.json') as rooms_data:
        return json.load(rooms_data)


def stuff_info():
    with open('stuff.json') as stuff_data:
        return json.load(stuff_data)
