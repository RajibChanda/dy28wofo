from distutils.core import setup
from setuptools import find_packages
setup(name='dy28wofo',
version='0.1',
author='DSSS',
author_email='rajib.chanda@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets'])