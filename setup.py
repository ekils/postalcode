from setuptools import setup, find_packages

setup(
    name = 'postalcode',
    packages = find_packages(),
    include_package_data=True,    # include everything in source control
    package_data = {'': '*.xlsx'},
    version = '1.6',
    description = 'pip install postalcode',
    author = 'ekils',
    author_email = 'bobobo746@hotmail.com',
    url = 'https://github.com/ekils/postalcode',
    download_url = 'https://github.com/ekils/postalcode.git',
    keywords = ['Good Project'],
    classifiers = [],
)
