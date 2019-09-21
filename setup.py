import os
import re
from setuptools import setup


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__), 'mailgun-validator', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in mailgun-validator/__init__.py')


setup(name='mailgun-validator',
      version=read_version(),
      description='Python wrapper for Mailgun email validation API',
      platforms=['POSIX'],
      author='Vladimir Troflianin',
      author_email='troflyaninvv@gmail.com',
      url='',
      packages=['mailgun-validator'],
      install_requires=[],
      dependency_links=[],
      include_package_data=True)
