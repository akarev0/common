import os

from flask import Blueprint, render_template, request, redirect, url_for, flash

from routes.products.form import AddNewProduct
from routes.products.utils import get_products_data, get_new_id, add_products_data

products = Blueprint('products', __name__, template_folder='template', static_folder='static',
                     static_url_path='/products/static')


@products.route('/product', methods=['GET', 'POST'])
def get_products():
    data = request.args
    filtered_list = []
    if data:
        for product in get_products_data():
            if product.get('price') == data.get('price'):
                filtered_list.append(product['name'])
        return render_template('price_filter.html', data=filtered_list)
    else:
        return render_template('all_products.html', data=get_products_data())


@products.route('/product/<string:value>')
def products_page(value):
    for product in get_products_data():
        if product.get('id') == value:
            name = product.get('name')
            price = product.get('price')
            desc = product.get('description')
            image = product.get('img_name')
            return render_template('product_page.html', name=name, price=price, desc=desc, image=image)
    return render_template('product_page.html')


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddNewProduct()
    if form.validate_on_submit():
        if request.method == 'POST':
            data = request.files['new_product_image']
            path = os.path.join('routes/products/static', data.filename)
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
            flash('Thank you! New product {} was add to our list'.format(name))
        return redirect(url_for('products.get_products'))
    return render_template('add_product.html', title='Add product', form=form)




