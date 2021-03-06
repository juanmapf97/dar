#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

requirements = ["Click>=6.0"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Alan Velasco",
    author_email="alanvelasco.a@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    description="Dar is a command line toolbelt for managing different project workflows.",
    entry_points={"console_scripts": ["dar=dar.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="dar",
    name="dar",
    packages=find_packages(include=["dar"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/alanbato/dar",
    version="0.1.0",
    zip_safe=False,
)
