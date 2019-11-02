from flask import Blueprint, render_template

from blueprint_products.utils import get_data


products = Blueprint('products', __name__, template_folder='template', static_folder='static')


@products.route('/products')
def get_products():
    return render_template('all_products.html')


@products.route('/apple')
def get_apple():
    return render_template('apple.html', data=get_data())


@products.route('/chocolate')
def get_chocolate():
    return render_template('chocolate.html', data=get_data())


@products.route('/egg')
def get_egg():
    return render_template('egg.html', data=get_data())


@products.route('/grapefruit')
def get_grapefruit():
    return render_template('grapefruit.html', data=get_data())


@products.route('/oatmeal')
def get_oatmeal():
    return render_template('oatmeal.html', data=get_data())
