#!/usr/bin/env python

from io import open
from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(name="dask-kubernetes",
      version="0.0.1",
      description="Dask Kubernetes",
      url="https://github.com/martindurant/dask-kubernetes",
      author="Martin Durant",
      author_email="mdurant@continuum.io",
      keywords='kubernetes',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      packages=['dask_kubernetes'],
      package_dirs={'dask_kubernetes': ['dask_kubernetes']},
      install_requires=['click'],
      zip_safe=False,
      package_data={'kubernetes': ['*.yaml']},
      include_package_data=True,
      long_description=readme,
      entry_points="""
        [console_scripts]
        dask-kubernetes=dask_kubernetes.cli.main:start
      """)
