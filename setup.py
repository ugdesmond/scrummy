import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
version = __import__('django').get_version()

setup(
    name='django-okoroscrumy',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple and intuitive virtual task board based on some concepts of Scrum that helps organize and manage your projects.',
    long_description=README,
    url='',
    author='Okoro Ugochukwu',
    author_email='ugdesmond@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)