import os
import sys
from setuptools import setup, find_packages

version = '1.4.1-alpha'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version,
                                                 version))
    os.system("git push --tags")
    sys.exit()

setup(
    name='django-user-sessions',
    version=version,
    description='Django sessions with a foreign key to the user',
    long_description=open('README.rst').read(),
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    url='http://github.com/Bouke/django-user-sessions',
    download_url='https://pypi.python.org/pypi/django-user-sessions',
    license='MIT',
    packages=find_packages(exclude=('example', 'tests',)),
    install_requires=['Django>=1.8'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Security',
    ],
)
