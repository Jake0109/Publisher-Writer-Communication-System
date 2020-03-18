from flask_caching import Cache
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

cache = Cache()
db = SQLAlchemy()
migrate = Migrate()
sess = Session()

def init_extensions(app):
    migrate.init_app(app,db)
    db.init_app(app)
    cache.init_app(app)
    sess.init_app(app)