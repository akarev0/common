from flask import Flask, render_template

from routes.Products.products import products
from routes.Supermarkets.supermarkets import supermarkets

app = Flask(__name__)

app.register_blueprint(products)
app.register_blueprint(supermarkets)


@app.route('/home')
def get_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
