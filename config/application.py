import os

from config.environment.development import DevelopmentConfig
from config.environment.production import ProductionConfig
from config.environment.testing import TestingConfig

app_config = {"production": ProductionConfig, "development": DevelopmentConfig, "test": TestingConfig}

app_env = os.getenv("LETSGO_ENV")
settings = app_config.get(app_env, DevelopmentConfig)()
