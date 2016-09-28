import warnings

from wheezy.http import HTTPResponse
from wheezy.http import WSGIApplication
from wheezy.routing import url
from wheezy.web.handlers import BaseHandler
from wheezy.web.middleware import bootstrap_defaults
from wheezy.web.middleware import path_routing_middleware_factory


class WelcomeHandler(BaseHandler):

    def get(self):
        response = HTTPResponse()
        response.write('Hello World!')
        return response


def welcome(request):
    response = HTTPResponse()
    response.write('Hello World!')
    return response


all_urls = [
    url('welcome', WelcomeHandler),
    #url('welcome', welcome),
]

warnings.simplefilter('ignore')
main = WSGIApplication(
    middleware=[
        bootstrap_defaults(url_mapping=all_urls),
        path_routing_middleware_factory
    ],
    options={}
)
