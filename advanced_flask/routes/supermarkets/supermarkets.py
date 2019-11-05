from flask import Blueprint, render_template

from routes.supermarkets.utils import get_supermarkets_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='template')


@supermarkets.route('/supermarket')
def get_supermarkets():
    return render_template('all_supermarkets.html')


@supermarkets.route('/supermarket/<value>')
def supermarket_page(value):
    for supermarket in get_supermarkets_data():
        if supermarket.get('id') == value:
            name = supermarket.get('name')
            location = supermarket.get('location')
            image = supermarket.get('img_name')
            return render_template('supermarket_page.html', name=name, location=location, image=image)
