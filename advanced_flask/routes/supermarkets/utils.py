import json
from json import JSONDecodeError


def get_supermarkets_data(path):
    try:
        with open(path) as supermarkets_data:
            return json.load(supermarkets_data)
    except (FileNotFoundError, ValueError):
        return []


def get_new_id(path):
    try:
        with open(path, 'r') as supermarkets_data:
            data = json.load(supermarkets_data)
        return str(max([int(item.get('id')) for item in data]) + 1)
    except JSONDecodeError:
        return "1"


def add_supermarket_data(path, data):
    with open(path, 'w') as supermarkets_data:
        json.dump(data, supermarkets_data, indent=4)
