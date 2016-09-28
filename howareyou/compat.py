import sys

PY3 = sys.version_info[0] >= 3
if PY3:
    from io import BytesIO
    ntob = lambda n, encoding: n.encode(encoding)
else:
    from cStringIO import StringIO as BytesIO
    ntob = lambda n, encoding: n
