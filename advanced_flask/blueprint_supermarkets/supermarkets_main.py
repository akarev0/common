from flask import Blueprint, render_template

from blueprint_supermarkets.utils_s import get_data


supermarkets = Blueprint('supermarkets', __name__, template_folder='template', static_folder='static')


@supermarkets.route('/supermarkets')
def get_supermarkets():
    return render_template('all_supermarkets.html')
