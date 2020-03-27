import os


def generate_db_uri(dbinfo):
    engine = dbinfo.get("engine")
    driver = dbinfo.get("driver")
    user = dbinfo.get("user")
    password = dbinfo.get("password")
    host = dbinfo.get("host")
    port = dbinfo.get("port")
    database = dbinfo.get("database")

    return f"{engine}+{driver}://{user}:{password}@{host}:{port}/{database}"


class baseConfig:
    DEBUG = False
    TESTING = False

    SECRET_KEY = "JAKE"

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class developConfig(baseConfig):
    DEBUG = True

    CACHE_TYPE = 'simple'

    SQLALCHEMY_DATABASE_URI = "sqlite:///D:/Publisher-Writer-Communication-System/database/test.db"


class testingConfig(baseConfig):
    DEBUG = True

    CACHE_TYPE = 'redis'

    dbinfo = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "jake0109",
        "host": "host",
        "port": 3306,
        "database": "flask",
    }

    SQLALCHEMY_DATABASE_URI = generate_db_uri(dbinfo)

envs = {
    "development": developConfig,
    "testing": testingConfig,
    "default": developConfig,
}

BASE_DIR = os.path.dirname(__file__)

SUPER_ADMINS = ["admin", "jake"]

UPLOAD_DIR = os.path.join(BASE_DIR, "static/uploads/")

print(UPLOAD_DIR)