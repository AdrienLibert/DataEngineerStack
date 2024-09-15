from setuptools import setup, find_packages

setup(
    name='kafka_pyspark_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyspark==3.5.2'
    ],
)