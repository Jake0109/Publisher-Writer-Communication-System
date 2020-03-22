from App.APIs.publisher import publisher_api
from App.APIs.writer import writer_api


def init_apis(app):
    writer_api.init_app(app)
    publisher_api.init_app(app)