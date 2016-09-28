from flask import Flask


main = Flask(__name__)


@main.route('/users/<name>')
def user(name):
    return 'User: %s' % name
