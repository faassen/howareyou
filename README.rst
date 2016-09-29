How Are You - Benchmarking Python Web Frameworks
================================================

This is a benchmark suite for various Python web frameworks.

Included:

* hello -- a simple URL without variables.

* variable -- respond to a URL with a single string variable.

* exception -- generate a 404 error by asking for a URL that doesn't exist.
  Reuses the ``hello`` applications.

To run them you can use the following::

  $ virtualenv --python=python2 env/py2
  $ source env/py2/bin/activate
  $ pip install -U pip setuptools
  $ pip install -r requirements.txt

You can now use the ``howareyou`` tool::

  $ howareyou

Without any arguments it runs the ``hello`` benchmarks against all
frameworks for which there is a test application implemented.

Benchmark results
-----------------

The benchmark runs 100,000 requests against each web framework, using
the WSGI directly. No real HTTP server is therefore involved, nor are
any requests handled in parallel -- it only means how much time the
framework takes in Python.

``ms`` is the amount of milliseconds it took to fulfill all 100,000
requests. ``rps`` is the amount of requests per second the framework
was able to sustain.

The benchmark also runs a single request with the profiler after this,
and reports in ``tcalls`` how many function calls the request took,
and in ``funcs`` how many different functions were used to handle the
request.

Options
-------

You use the ``-b`` flag to select the benchmark to run, for instance::

  $ howareyou -b variable

You use the ``-f`` flag to restrict the frameworks to benchmark, for
instance::

  $ howareyou benchmark.py -f morepath -f flask

to benchmark just Flask and Morepath.

You can use the ``-n`` flag to change the number of requests to use
in the benchmark::

  $ howareyou -n 1000

the default is 100000.

With the ``-p`` flag the tool also generates profile information on
which functions it spent the most time in.

You can give it a ``-h`` for help. With ``-p`` you can select the
benchmark, and with ``-f`` you can select the frameworks against which
to run it.

Testing implementations
-----------------------

To check whether an implementation of a benchmark in a particular
framework actually is correct, you can use the ``trialserver``
command. For example, to check whether Morepath behaves correctly with
the ``hello`` benchmark use::

  $ trialserver hello morepath

It starts up a web server on port 8000. You can point your web browser
to it and make experimental requests.

History
-------

This benchmark is adapted from the 01-hello example by Andriy
Kornatskyy, author of wheezy.web.

https://bitbucket.org/akorn/helloworld

I've simplified things considerably. I only install web frameworks
that seem to be reasonably popular and that are easy to install from
PyPI with pip. I've excluded some frameworks because they seemed very
slow; it's possible they aren't actually slow but that the benchmark
code was broken, but I didn't want to bother.

In addition there's Morepath_, authored by myself, and `wheezy.web`_,
as Andriy wrote that.

.. _Morepath: http://morepath.readthedocs.io

.. _wheezy.web: https://pythonhosted.org/wheezy.web/

A previous iteration of this tool just included the ``hello``
test. I've since expanded the tool so you can run multiple benchmarks
with it.
