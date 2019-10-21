from config.application import settings
from databases import Database
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
database = Database(settings.SQLALCHEMY_DATABASE_URI)
