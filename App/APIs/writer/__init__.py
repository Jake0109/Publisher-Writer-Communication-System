from flask_restful import Api

from App.APIs.writer.writter_API import writerResource

writer_api = Api(prefix='/writers/')

writer_api.add_resource(writerResource, '/writers/')
