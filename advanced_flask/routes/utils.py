import json


def get_products_data():
    with open("routes/products.json") as file:
        return json.load(file)


def get_supermarkets_data():
    with open("routes/supermarkets.json") as file:
        return json.load(file)
