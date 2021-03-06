from flask import Flask

from App.APIs import init_apis
from App.Views import init_blueprint
from App.extensions import init_extensions
from App.settings import envs



def init_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))

    init_apis(app)
    init_extensions(app)
    init_blueprint(app)
    return app
