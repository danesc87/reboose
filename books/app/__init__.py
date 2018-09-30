#!/usr/bin/python3
# Books MicroService App Init
"""
 Author: Daniel Córdova A.
"""

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, error_handler
from app.views import author_views
from app.views import book_settings_views
from app.views import book_views
