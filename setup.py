try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My project',
    'author': 'Amy'
    'url': 'url to get it at'
    'download_url': "where to download it"
    'author_email': 'my email'
    'version': '0.1'
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': []
    'name': 'projectname'
}

setup(**config)
