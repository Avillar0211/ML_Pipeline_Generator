from setuptools import find_packages, setup

setup(
    name='ML_Pipeline_Generator',
    packages=find_packages(),
    version='1.0',
    description='A Python library to create Machine Learning Pipelines',
    install_requires=['pandas','wheel','nose2', 'numpy', 'sklearn'],
    author='Me',
)