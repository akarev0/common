import json


def get_data():
    with open("blueprint_products/products.json") as file:
        return json.load(file)
