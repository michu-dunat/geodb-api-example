from setuptools import setup

setup(
    name='geodb-api-consume-package',
    version='1.0',
    packages=['geodb_lib'],
    license='MIT',
    description='Python package for consuming GeoDB API',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='',
    author='Michał Dunat',
    author_email='kontaktmichaldunat@gmail.com'
)