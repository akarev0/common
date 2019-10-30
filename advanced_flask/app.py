from flask import Flask, render_template

from blueprint.main import products

app = Flask(__name__)

app.register_blueprint(products)


@app.route('/home')
def get_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
