# -*- coding: utf-8 -*-
import re

from setuptools import find_packages, setup


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not (re.match('\s*#', line) or re.match('-e', line))  # noqa
        ]


requirements = load_reqs('requirements.txt')

setup(
    name='fentpais',
    version=open('./VERSION').read().strip(),
    long_description="Fent Pais",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url='https://iskra.cat',
    license='MIT',
    setup_requires=[
        'pytest-runner',
    ],
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements
)
