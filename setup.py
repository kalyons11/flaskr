"""
Package setup file.
"""

from setuptools import setup, find_packages

setup(name='flaskr',
      version='1.0.0',
      author='Kevin Lyons',
      description='Flaskr tutorial.',
      url='hhttps://github.com/kalyons11/flaskr',
      author_email='kevinandrewlyons@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'flask'
      ]
      )
