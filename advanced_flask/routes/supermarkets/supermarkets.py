from flask import Blueprint, render_template

from routes.supermarkets.utils import get_supermarkets_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='template')


@supermarkets.route('/supermarkets')
def get_supermarkets():
    return render_template('all_supermarkets.html')


@supermarkets.route('/karavan')
def get_karavan_page():
    return render_template('karavan.html', data=get_supermarkets_data())


@supermarkets.route('/moct-city')
def get_moct_city_page():
    return render_template('moct-city.html', data=get_supermarkets_data())


@supermarkets.route('/plaza')
def get_plaza_page():
    return render_template('plaza.html', data=get_supermarkets_data())


@supermarkets.route('/pravda')
def get_pravda_page():
    return render_template('pravda.html', data=get_supermarkets_data())


@supermarkets.route('/fabrika')
def get_fabrika_page():
    return render_template('fabrika.html', data=get_supermarkets_data())
