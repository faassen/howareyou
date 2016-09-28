from pyramid.config import Configurator
from pyramid.response import Response


def user(request):
    return Response('User: %(name)s' % request.matchdict)


config = Configurator()
config.add_route('user', '/users/{name}')
config.add_view(user, route_name='user')
main = config.make_wsgi_app()
