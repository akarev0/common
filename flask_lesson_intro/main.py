from flask import Flask, render_template
from flask_lesson_intro.utils import get_data


app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html")


@app.route('/alarm_clock')
def alarm_clock_page():
    return render_template('alarm_clock.html')


@app.route('/headphones')
def headphones_page():
    return render_template('headphones.html')


@app.route('/ipod')
def ipod_page():
    return render_template('ipod.html')


@app.route('/calculator')
def calculator_page():
    return render_template('calculator.html')


@app.route('/coffeemaker')
def coffeemaker_page():
    return render_template('coffeemaker.html')


@app.route('/battery_charger')
def battery_charger_page():
    return render_template('battery_charger.html')


@app.route('/author')
def author_page():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=True)
