from setuptools import setup, find_packages

setup(name='super_fun_converter',
    version='0.0.1',
    url='http://github.com/CitrineInformatics/citrine-python-converter-template',
    description='This converter does something',
    author='This converter was written by someone',
    author_email='maxhutch@citrine.io',
    packages=find_packages(),
    install_requires=[
        'pypif',
    ],
    entry_points={
        'citrine.dice.converter': [
            'super_fun = super_fun_converter.converter',
        ],
    },
)
