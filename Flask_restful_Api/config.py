import os


class Config:
    SECRET_KEY = 'secret_key'


class TestConfig:
    SECRET_KEY = 'secret_test_key'


class ProductionConfig:
    SECRET_KEY = 'secret_production_key'


def necessary_config():
    env = os.environ.get('ENV')
    if env == 'TEST':
        return TestConfig
    elif env == 'PROD':
        return ProductionConfig
    else:
        return Config


