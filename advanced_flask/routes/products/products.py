import os

from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

from routes.products.utils import get_products_data

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
    form = AddNewProduct(request.form)
    name = form.new_product_name.data
    desc = form.new_product_description.data
    price = form.new_product_price.data
    if form.validate_on_submit():
        if request.method == 'POST':
            data = request.files['data']
            path = os.path.join('static', data.filename)
            data.save(path)
        return redirect(url_for('get_products'))
    return render_template('add_product.html', title='Add product', form=form)


class AddNewProduct(FlaskForm):
    new_product_name = StringField(validators=[DataRequired()])
    new_product_description = StringField(validators=[DataRequired()])
    new_product_image = FileField(validators=[FileRequired()])
    new_product_price = StringField(validators=[DataRequired()])
    submit = SubmitField('Send')
