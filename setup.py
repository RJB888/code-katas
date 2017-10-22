"""."""

from setuptools import setup

setup(

    name='day of code',
    description='Day of code katas.',
    package_dir={'': 'src'},
    author='Robert Bronson',
    author_email='robert.j.bronson@gmail.com',
    py_modules=['rot_13', 'coordinates...... ** all my modules (.py files)**'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
