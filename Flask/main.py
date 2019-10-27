from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/vegetables')
def get_vegetables():
    list_of_vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template("vegetables.html", data=list_of_vegetables)


@app.route('/fruits')
def get_fruits():
    fruits_list = ["melon", "apple", "strawberry", "grape"]
    return render_template("fruits.html", data=fruits_list)


if __name__ == "__main__":
    app.run(debug=True)
