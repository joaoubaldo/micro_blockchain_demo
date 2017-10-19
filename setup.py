import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'requirements.txt')) as f:
    requires = f.read().splitlines()

tests_require = requires + [
    'pylint'
]

setup(
    name='micro_blockchain_demo',
    version='0.0.1',
    description='Micro blockchain demo',
    long_description=README + '\n',
    classifiers=[
        "Programming Language :: Python"
    ],
    author='Joao Coutinho',
    author_email='me@joaoubaldo.com',
    url='https://b.joaoubaldo.com',
    keywords='blockchain demo example',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'micro_blockchain_demo = micro_blockchain_demo.tool:main']
        }
)
