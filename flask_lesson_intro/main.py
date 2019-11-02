from flask import Flask, render_template

from utils import get_data


app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/<value>')
def return_any_route(value):
    for pages in get_data():
        if pages.get('title') == value:
            content = pages.get('text')
            return render_template("any.html", value=value, data=content)


if __name__ == "__main__":
    app.run(debug=True)
