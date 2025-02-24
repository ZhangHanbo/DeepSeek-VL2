from distutils.core import setup
from setuptools import find_packages

setup(
    name='deepseek_vl2',
    version='0.0.0',
    packages=find_packages(exclude=["images"]),
    license='MIT License',
    long_description=open('README.md').read(),
)
