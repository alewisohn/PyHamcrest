import sys
import os
import re

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def local(fname):
    return os.path.join(os.path.dirname(__file__), fname)

def read(fname):
    return open(local(fname)).read()

# On Python 3, we can't "from hamcrest import __version__" (get ImportError),
# so we extract the variable assignment and execute it ourselves.
fh = open(local('src/hamcrest/__init__.py'))
try:
    for line in fh:
        if re.match('__version__.*', line):
            exec(line)
finally:
    if fh:
        fh.close()

extra_attributes = {}
# if sys.version_info >= (3,):
#     extra_attributes['use_2to3'] = True

params = dict(
    name='PyHamcrest',
    version=__version__,  #flake8:noqa
    author='Chris Rose',
    author_email='offline@offby1.net',
    description='Hamcrest framework for matcher objects',
    license='New BSD',
    platforms=['All'],
    keywords='hamcrest matchers pyunit unit test testing unittest unittesting',
    url='https://github.com/hamcrest/PyHamcrest',
    download_url='http://pypi.python.org/packages/source/P/PyHamcrest/PyHamcrest-%s.tar.gz' % __version__,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    provides=['hamcrest'],
    long_description=read('README.rst'),
    install_requires=['setuptools', 'six'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        ],
    **extra_attributes
    )

all_params = dict(params.items(), **extra_attributes)
setup(**all_params)
