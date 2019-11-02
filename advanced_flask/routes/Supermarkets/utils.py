import json


def get_supermarkets_data():
    with open("routes/Supermarkets/supermarkets.json") as file:
        return json.load(file)
