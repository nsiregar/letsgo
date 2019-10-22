from config.environment.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/letsgo_development"
    BCRYPT_LOG_ROUND = 4
