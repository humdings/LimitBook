#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'limitbook'
DESCRIPTION = "Simple limit order book and matching engine."
MAINTAINER = 'David Edwards'
MAINTAINER_EMAIL = 'humdings@gmail.com'
AUTHOR = 'David Edwards'
AUTHOR_EMAIL = 'humdings@gmail.com'
URL = "https://github.com/humdings/LimitBook"
VERSION = "0.0.1"

classifiers = [
    'Programming Language :: Python',
    'Operating System :: OS Independent'
]

if __name__ == "__main__":
    setup(name=DISTNAME,
          version=VERSION,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          url=URL,
          packages=find_packages('.', include=['limitbook', 'limitbook.*']),
          classifiers=classifiers,
)

