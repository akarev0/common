from flask import Flask, render_template

from routes.products.products import products
from routes.supermarkets.supermarkets import supermarkets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.register_blueprint(products)
app.register_blueprint(supermarkets)


@app.route('/')
def get_home_page():
    return render_template('home.html')


@app.errorhandler(404)
def handle_404(error):
    return render_template('error_page.html')


if __name__ == "__main__":
    app.run(debug=True)
