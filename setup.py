from setuptools import setup

required_packages = [
    'setuptools',
    'gevent',
    'werkzeug',
    'Flask',
    'Flask-RESTful',
    'Sphinx',
    'Flask-Security',
    'anyjson',
    'coverage',
    'docutils',
    'requests',
    'six',
    'sphinx-bootstrap-theme',
    'sphinxcontrib-httpdomain',
    'flask-peewee'
]

setup(
    name='lxcapi.lxcapi',
    description='Secure remote lxc API',
    version='0.0.1',
    packages=['lxcapi',
              'lxcapi.lxcapi'],
    namespace_packages=['lxcapi'],
    install_requires=required_packages,
    extras_require={
        'test': [
            'nose',
            'ddbmock',
        ]
    }
)
