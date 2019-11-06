import json
import os

from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from routes.products.form import AddNewProduct
from routes.products.utils import get_products_data, get_new_id, add_products_data


products = Blueprint('products', __name__, template_folder='template', static_folder='static')


@products.route('/product', methods=['GET', 'POST'])
def get_products():
    return render_template('all_products.html')


@products.route('/product/<value>')
def products_page(value):
    for product in get_products_data():
        if product.get('id') == value:
            name = product.get('name')
            price = product.get('price')
            desc = product.get('description')
            image = product.get('img_name')
            return render_template('product_page.html', name=name, price=price, desc=desc, image=image)


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddNewProduct()
    if form.validate_on_submit():
        if request.method == 'POST':
            data = request.files['new_product_image']
            path = os.path.join('static', data.filename)
            data.save(path)
            name = form.new_product_name.data
            desc = form.new_product_description.data
            image = form.new_product_image.data
            price = form.new_product_price.data
            new_id = get_new_id('routes/products/products.json')
            result = {'id': new_id, 'name': name, 'desc': desc, "img_name": image.filename, "price": price}
            all_products = get_products_data()
            all_products.append(result)
            add_products_data('routes/products/products.json', all_products)
        return redirect(url_for('products.get_products'))
    return render_template('add_product.html', title='Add product', form=form)




