import io
from setuptools import setup, find_packages

long_description = '\n'.join((
    io.open('README.rst', encoding='utf-8').read(),
    io.open('CHANGES.txt', encoding='utf-8').read()
))

setup(
    name='howareyou',
    version='0.1.dev0',
    description="Benchmarking Python web frameworks",
    long_description=long_description,
    author="Martijn Faassen",
    author_email="faassen@startifact.com",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'setuptools',
    ],
    entry_points={
        'console_scripts': [
            'howareyou = howareyou.main:main',
            'trialserver = howareyou.trial:main',
        ],
    }
)
