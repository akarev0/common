from flask import Flask, render_template

from blueprint_products.products_main import products
from blueprint_supermarkets.supermarkets_main import supermarkets

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(supermarkets)


@app.route('/home')
def get_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
