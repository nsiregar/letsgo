class BaseConfig:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/base"
    BCRYPT_LOG_ROUND = 13
