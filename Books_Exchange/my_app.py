from flask import Flask


def create_app():
    my_app = Flask(__name__)
    return my_app


if __name__ == "__main__":
    create_app().run()


