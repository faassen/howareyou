from __future__ import print_function

import os
import sys

try:
    import cProfile as profile
except ImportError:
    import profile

from pstats import Stats
from timeit import timeit

from .benchmarks import benchmarks


def start_response(status, headers, exc_info=None):
    return None


def run(benchmark, frameworks, number, do_profile):
    print("Benchmark :", benchmark)
    print("Frameworks:", ', '.join(frameworks))
    environ = benchmarks[benchmark]
    try:
        environ, benchmark_dir = environ
    except ValueError:
        benchmark_dir = benchmark

    sys.path[0] = '.'
    path = os.path.join(os.getcwd(), benchmark_dir)
    print("                ms     rps  tcalls  funcs")
    for framework in frameworks:
        framework_path = os.path.join(path, framework)
        if not os.path.isdir(framework_path):
            print("No benchmark for:", framework)
            continue
        if framework != 'wsgi':
            try:
                __import__(framework)
            except ImportError:
                print("%s not installed" % framework)
                continue
        os.chdir(framework_path)
        main = __import__('app', None, None, ['main']).main
        f = lambda: list(main(environ.copy(), start_response))
        time = timeit(f, number=number)
        st = Stats(profile.Profile().runctx(
            'f()', globals(), locals()))
        print("%-11s %6.0f %7.0f %7d %6d" % (
            framework, 1000 * time,
            number / time, st.total_calls, len(st.stats)))
        if do_profile:
            st = Stats(profile.Profile().runctx(
                'timeit(f, number=number)', globals(), locals()))
            st.strip_dirs().sort_stats('time').print_stats(10)
        del sys.modules['app']
