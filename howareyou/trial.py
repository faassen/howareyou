import argparse
from wsgiref.simple_server import make_server
import os
import sys
from .benchmarks import benchmarks
from .main import known_frameworks


def main():
    parser = argparse.ArgumentParser(
        "Run test server for benchmark and framework")
    parser.add_argument('benchmark', help="the benchmark to run",
                        choices=benchmarks.keys())
    parser.add_argument('framework', help="the web framework to run",
                        choices=known_frameworks)

    args = parser.parse_args()
    benchmark = args.benchmark
    framework = args.framework

    path = os.getcwd()

    framework_path = os.path.join(path, benchmark, framework)

    if not os.path.isdir(framework_path):
        parser.error("Test code does not exist for framework: %s" % framework)
        return

    sys.path[0] = framework_path

    os.chdir(framework_path)

    main = __import__('app', None, None, ['main']).main

    httpd = make_server('', 8000, main)
    print("Serving %s on port 8000..." % framework)

    httpd.serve_forever()
