import json


def get_data():
    with open("blueprint_supermarkets/supermarkets.json") as file:
        return json.load(file)
