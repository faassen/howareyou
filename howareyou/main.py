from __future__ import print_function
import argparse
from .run import run
from .benchmarks import benchmarks

known_frameworks = [
    'bottle',
    'django',
    'falcon',
    'flask',
    'morepath',
    'pyramid',
    'tornado',
    'wheezy.web',
    'wsgi',
]


def main():
    parser = argparse.ArgumentParser("Benchmark Python web frameworks.")
    parser.add_argument(
        '-b', '--benchmark', default='hello',
        choices=benchmarks.keys(),
        help="Benchmark to run")
    parser.add_argument(
        '-f', '--framework', action='append',
        choices=known_frameworks,
        help='Restrict frameworks to benchmark')
    parser.add_argument(
        '-n', '--number', type=int, default=100000,
        help='Number of requests used for timing')
    parser.add_argument(
        '-p', '--profile', action='store_true',
        help='Also generate profile information')

    args = parser.parse_args()
    benchmark = args.benchmark
    frameworks = args.framework
    if not frameworks:
        frameworks = sorted(known_frameworks)
    run(benchmark, frameworks, args.number, args.profile)
