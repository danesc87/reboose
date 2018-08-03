#!flask/bin/python
from migrate.versioning import api
from config import Config

SQLALCHEMY_MIGRATE_REPO = Config.SQLALCHEMY_MIGRATE_REPO
SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
database_version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Currente database version is: ' + str(database_version))