#!/usr/bin/env python
# old functional:
from distutils.core import setup
import setuptools

import os


def read_requirements():
    """parses requirements from requirements.txt"""
    reqs_path = os.path.join(".", "requirements.txt")
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs


setup(
    name="academic author network",
    version="1.0",
    description="heavily applied scraping, crawling and language analysis, tightly coupled with the goal of analysing scientific discourse",
    author="various",
    author_email="don_t_email_we_are_on_github@gmail.com",
    url="https://github.com/russelljjarvis/ScienceAccessibility",
    packages=setuptools.find_packages(),
)
