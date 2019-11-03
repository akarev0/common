from flask import Blueprint, render_template, request, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from routes.products.utils import get_products_data

products = Blueprint('products', __name__, template_folder='template', static_folder='static')


@products.route('/products', methods=['GET', 'POST'])
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


@products.route('/add_product')
def add_product():
    form = AddNewProduct(request.form)
    if form.validate_on_submit():
        flash('New product added to list {}'.format(form.new_product_name.data, form.new_product_description.data,
                                                    form.new_product_price.data))
        return redirect('/products')
    return render_template('add_product.html', title='Add product', form=form)


class AddNewProduct(FlaskForm):
    new_product_name = StringField('name', validators=[DataRequired()])
    new_product_description = StringField('description', validators=[DataRequired()])
    new_product_src = StringField('screen', validators=[DataRequired()])
    new_product_price = StringField('price', validators=[DataRequired()])
    submit = SubmitField('Send')
