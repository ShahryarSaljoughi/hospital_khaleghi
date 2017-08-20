import os


basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = "you-will-never-guess"

DB_USER = 'postgres'
DB_PASSWORD = 'amin1672'
DB_HOST = 'localhost'

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:amin1672@127.0.0.1:5432/hospitalDatabase"
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')