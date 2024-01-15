from setuptools import find_packages, setup

setup(
    name='ML_Pipeline_Generator',
    packages=find_packages(),
    version='1.0',
    description='My first Python library',
    install_requires=['pandas','wheel','nose2', 'numpy', 'sklearn'],
    author='Me',
)