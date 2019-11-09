import json
from json import JSONDecodeError


def get_products_data():
    with open("routes/products/products.json") as product_data:
        return json.load(product_data)


def get_new_id(path):
    try:
        with open(path, 'r') as product_data:
            data = json.load(product_data)
        return str(max([int(item.get('id')) for item in data]) + 1)
    except JSONDecodeError:
        return 1


def add_products_data(path, data):
    with open(path, 'w') as product_data:
        json.dump(data, product_data, indent=4)
