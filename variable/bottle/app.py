from bottle import route, default_app


@route('/users/<name>')
def index(name):
    return 'User: %s' % name


main = default_app()
