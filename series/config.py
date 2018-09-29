#!/usr/bin/python3
# Configuration for Series MicroService
"""
 Author: Daniel Córdova A.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'series.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
