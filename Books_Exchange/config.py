import os


class Config:
    PG_USER = "librarian_1"
    PG_PASSWORD = "password"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "book_exchange"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    DEBUG = True


class DevConfig(Config):
    TEST_VALUE = "DEV_CONFIG_VALUE"


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config
