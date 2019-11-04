import os

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired

from routes.products.utils import get_products_data

products = Blueprint('products', __name__, template_folder='template', static_folder='static')


@products.route('/product', methods=['GET', 'POST'])
def get_products():
    return render_template('all_products.html')


@products.route('/apple')
def get_apple():
    return render_template('apple.html', data=get_products_data())


@products.route('/chocolate')
def get_chocolate():
    return render_template('chocolate.html', data=get_products_data())


@products.route('/egg')
def get_egg():
    return render_template('egg.html', data=get_products_data())


@products.route('/grapefruit')
def get_grapefruit():
    return render_template('grapefruit.html', data=get_products_data())


@products.route('/oatmeal')
def get_oatmeal():
    return render_template('oatmeal.html', data=get_products_data())


@products.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = AddNewProduct(request.form)
    print(request.files)
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
