import json


def get_products_data():
    with open("routes/Products/products.json") as file:
        return json.load(file)
