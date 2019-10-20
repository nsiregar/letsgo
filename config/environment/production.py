from config.environment.base import BaseConfig
from starlette.config import Config


class ProductionConfig(BaseConfig):
    config = Config(".env")
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
