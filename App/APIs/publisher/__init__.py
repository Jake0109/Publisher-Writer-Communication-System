from flask_restful import Api

from App.APIs.publisher.Topic_API import topicResource, topicsResource
from App.APIs.publisher.publisher_API import publisherResource, publishersResource

publisher_api = Api(prefix="/publisher/")

publisher_api.add_resource(publisherResource, '/publisher/')
publisher_api.add_resource(publishersResource, '/publishers/')
publisher_api.add_resource(topicResource, '/topic/')
publisher_api.add_resource(topicsResource, '/topics/')