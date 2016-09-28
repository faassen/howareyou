
import sys


PY3 = sys.version_info[0] >= 3

if PY3:  # pragma: nocover
    b = lambda s: s.encode('latin1')
else:  # pragma: nocover
    b = lambda s: s


def welcome(env, start_response):
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', '12')
    ])
    return [b('Hello World!')]


def main(env, start_response):
    if env['PATH_INFO'] == '/welcome':
        return welcome(env, start_response)
    start_response('404 Not Found', [
        ('Content-Type', 'text/html'),
        ('Content-Length', '0')
    ])
    return [b('')]
