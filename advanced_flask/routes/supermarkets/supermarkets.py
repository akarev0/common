import os

from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.utils import redirect

from routes.supermarkets.form import AddNewSupermarket
from routes.supermarkets.utils import get_supermarkets_data, get_new_id, add_supermarket_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='template', static_folder='static',
                         static_url_path='/supermarkets/static')


@supermarkets.route('/supermarket')
def get_supermarkets():
    return render_template('all_supermarkets.html', data=get_supermarkets_data())


@supermarkets.route('/supermarket/<int:value>')
def supermarket_page(value):
    for supermarket in get_supermarkets_data():
        if supermarket.get('id') == value:
            name = supermarket.get('name')
            location = supermarket.get('location')
            image = supermarket.get('img_name')
            return render_template('supermarket_page.html', name=name, location=location, image=image)


@supermarkets.route('/add_supermarket', methods=['GET', 'POST'])
def add_supermarket():
    form = AddNewSupermarket()
    if form.validate_on_submit():
        if request.method == 'POST':
            data = request.files['new_supermarket_image']
            path = os.path.join('routes/supermarkets/static', data.filename)
            data.save(path)
            name = form.new_supermarket_name.data
            location = form.new_supermarket_location.data
            image = form.new_supermarket_image.data
            new_id = get_new_id('routes/supermarkets/supermarkets.json')
            result = {'id': new_id, 'name': name, 'location': location, "img_name": image.filename}
            all_supermarkets = get_supermarkets_data()
            all_supermarkets.append(result)
            add_supermarket_data('routes/supermarkets/supermarkets.json', all_supermarkets)
            flash('Thank you! New supermarket {} was add to our list'.format(name))
        return redirect(url_for('supermarkets.get_supermarkets'))
    return render_template('add_supermarket.html', title='Add supermarket', form=form)
