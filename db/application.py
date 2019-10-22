from config.application import settings
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return f"{ cls.__name__.lower() }s"


Base = declarative_base(cls=BaseModel)
database = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

Session = sessionmaker()
Session.configure(bind=database)
Session.configure(autocommit=False)
Session.configure(autoflush=False)

session = Session()
