from setuptools import setup, find_packages


setup(
    name='krait-dash-test',
    author='Camden',
    author_email='richtercamden@gmail.com',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click'],
    tests_require=['flake8', 'mypy', 'pytest-cov', 'pytest'],
    extras_require={
        'tests': ['flake8', 'mypy', 'pytest-cov', 'pytest'],
    },
    entry_points={
        'console_scripts': ['krait-dash-test = krait_dash_test.main:main']
    },
)
