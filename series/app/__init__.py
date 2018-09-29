#!/usr/bin/python3
# Series MicroService App Init
"""
 Author: Daniel Córdova A.
"""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, error_handler
from app.views import series_settings_views, series_views
