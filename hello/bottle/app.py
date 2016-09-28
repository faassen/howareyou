from bottle import route, default_app


@route('/welcome')
def index():
    return 'Hello World!'


main = default_app()
