from flask import Blueprint, render_template

products = Blueprint('products', __name__, template_folder='template')


@products.route('/products')
def get_products():
    return render_template('all_products.html')


@products.route('/apple')
def get_apple():
    return render_template('apple.html')


@products.route('/chocolate')
def get_chocolate():
    return render_template('chocolate.html')


@products.route('/egg')
def get_egg():
    return render_template('egg.html')


@products.route('/grapefruit')
def get_grapefruit():
    return render_template('grapefruit.html')


@products.route('/oatmeal')
def get_oatmeal():
    return render_template('oatmeal.html')
