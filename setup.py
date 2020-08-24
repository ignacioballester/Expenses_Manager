from setuptools import setup
setup(
    name = 'ExpensesManager',
    version = '0.1.0',
    packages = ['ExpensesManager'],
    entry_points = {
        'console_scripts': [
            'ExpensesManager = ExpensesManager.__main__:main'
        ]
    })