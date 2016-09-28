from .hello import environ as hello_environ
from .variable import environ as variable_environ
from .notfound import environ as notfound_environ

benchmarks = {
    'hello': hello_environ,
    'variable': variable_environ,
    'notfound': (notfound_environ, 'hello')
}
