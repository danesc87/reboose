#!/usr/bin/python3
# Series Microservice App Init
'''
Author: Daniel Córdova A.
'''

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, error_handler
from app.views import serie_settings_views
