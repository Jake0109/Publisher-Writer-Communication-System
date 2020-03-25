from flask_restful import Api

from App.APIs.writer.writter_API import writerResource, writersResource

writer_api = Api(prefix='/writer/')

writer_api.add_resource(writerResource, '/writer/')
writer_api.add_resource(writersResource, '/writers/')
