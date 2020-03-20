def generate_dburi(dbinfo):
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

    CACHE_TYPE = 'simple'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class developConfig(baseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///D:/Publisher-Writer-Communication-System/database/test.db"


class testingConfig(baseConfig):
    DEBUG = True

    dbinfo = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "jake0109",
        "host": "host",
        "port": 3306,
        "database": "flask",
    }

    SQLALCHEMY_DATABASE_URI = generate_dburi(dbinfo)

envs = {
    "development": developConfig,
    "testing": testingConfig,
    "default": developConfig,
}
