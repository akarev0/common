import json


def get_supermarkets_data():
    with open("routes/supermarkets/supermarkets.json") as file:
        return json.load(file)
