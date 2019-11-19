class Config:
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "practice"
    PG_PASSWORD = "1"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "films"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = "practice"
    PG_PASSWORD = "1"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "test_films"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config(prod="defualt"):
    if prod == "TEST":
        return TestConfig
    return Config
