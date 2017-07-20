from setuptools import setup, find_packages

setup(
    name = 'postalcode',
    #packages = ['tryanderror'],
    packages = find_packages(),
    version = '1.2',
    description = 'pip install postalcode',
    author = 'ekils',
    author_email = 'bobobo746@hotmail.com',
    url = 'https://github.com/ekils/postalcode',
    download_url = 'https://github.com/ekils/postalcode.git',
    keywords = ['Good Project'],
    classifiers = [],
    package_data = {'postalcode': ['*.xlsx']},
)
