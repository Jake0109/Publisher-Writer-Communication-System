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
    DEBBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class developConfig(baseConfig):
    DEBBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:////database/sqlite.db"


class testingConfig(baseConfig):
    DEBBUG = True

    dbinfo = {
        "engine": "mysql",
        "driver": "pymysql",
        "user": "user",
        "password": "password",
        "host": "host",
        "port": 3306,
        "database": "database",
    }

    SQLALCHEMY_DATABASE_URI = generate_dburi(dbinfo)

envs = {
    "development": developConfig,
    "testing": testingConfig,
    "default": developConfig,
}
