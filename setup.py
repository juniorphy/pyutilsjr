from setuptools import setup, find_packages
import os

PFCT_VERSION = '0.0.1'

CLASSIFIERS = [
    "Development Status :: 1 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 2.7",
    "Topic :: Software Development :: Libraries :: Python Modules",
    ]

PACKAGE_DATA = {'pyutilsjr': ['script/*','utils/*']}

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pyutilsjr',
      version=PFCT_VERSION,
      description='utils script to everyday programming',
      author='Fco Vasconcelos Jr & Marcelo Rodrigues',
      author_email='juniorphy@gmail.com',
      url='none',
      keywords='Climate, Statistics, Maps, Plots',
      license='GPLv3',
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      package_data=PACKAGE_DATA)
