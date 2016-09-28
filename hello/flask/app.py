from flask import Flask


main = Flask(__name__)


@main.route('/welcome')
def welcome():
    return 'Hello World!'
