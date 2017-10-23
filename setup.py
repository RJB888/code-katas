"""."""

from setuptools import setup

setup(

    name='sum of nth terms',
    description='Sum of Nth terms kata.',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['sum_of_nth_terms'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
