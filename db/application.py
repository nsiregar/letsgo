from config.application import settings
from databases import Database
from sqlalchemy import MetaData

metadata = MetaData()
database = Database(settings.SQLALCHEMY_DATABASE_URI)
