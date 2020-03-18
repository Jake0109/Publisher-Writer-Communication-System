from flask import Blueprint

blueprint = Blueprint("blue", __name__)

def init_blueprint(app):
    app.register_blueprint(blueprint)

@blueprint.route('/')
def hello_world():
    return 'Hello World!'
