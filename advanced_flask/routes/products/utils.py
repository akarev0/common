import json
from json import JSONDecodeError


def get_products_data():
    with open("routes/products/products.json") as file:
        return json.load(file)


def get_new_id(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
        return max([int(item.get('id')) for item in data]) + 1
    except JSONDecodeError:
        return 1


def add_products_data(path, data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
