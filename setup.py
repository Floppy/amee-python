from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='AMEE',
      version=version,
      description="A python egg for accessing the AMEE carbon calculator",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='amee carbon',
      author='James Smith',
      author_email='james@amee.cc',
      url='http://www.amee.com',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
