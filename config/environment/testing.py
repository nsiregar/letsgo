from config.environment.base import BaseConfig


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@db:5432/letsgo_testing"
