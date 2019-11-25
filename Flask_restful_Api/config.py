import os


class Config:
    SECRET_KEY = 'secret_key'
    DEBUG = True


class TestConfig:
    SECRET_KEY = 'secret_test_key'
    DEBUG = True


class ProductionConfig:
    SECRET_KEY = 'secret_production_key'
    DEBUG = False


def necessary_config():
    env = os.environ.get('ENV')
    config = {
        'TEST': TestConfig,
        'PROD': ProductionConfig,
        '': Config
    }
    return config.get(env)
