from starlette.config import Config


class BaseConfig(object):
    config = Config(".env")
    TESTING = False
    DEBUG = False
