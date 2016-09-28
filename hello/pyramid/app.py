from pyramid.config import Configurator
from pyramid.response import Response


def welcome(request):
    return Response('Hello World!')


config = Configurator()
config.add_route('welcome', '/welcome')
config.add_view(welcome, route_name='welcome')
main = config.make_wsgi_app()
