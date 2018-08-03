#!flask/bin/python
from migrate.versioning import api
from config import Config

SQLALCHEMY_MIGRATE_REPO = Config.SQLALCHEMY_MIGRATE_REPO
SQLALCHEMY_DATABASE_URI = Config.SQLALCHEMY_DATABASE_URI

database_version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, database_version-1)
database_version = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version is: ' + str(database_version))