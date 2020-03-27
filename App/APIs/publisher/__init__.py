from flask_restful import Api

from App.APIs.publisher.PublisherContracts_API import PubContractResource, PubContractsResource
from App.APIs.publisher.Topic_API import topicResource, topicsResource
from App.APIs.publisher.publisher_API import publisherResource, publishersResource
from App.APIs.publisher.publisher_tag_API import pubTagRelationResource

publisher_api = Api(prefix="/publisher/")

publisher_api.add_resource(publisherResource, '/publisher/<int:publisher_id>/')
publisher_api.add_resource(publishersResource, '/publishers/')

publisher_api.add_resource(topicResource, '/topic/<int:topic_id>/')
publisher_api.add_resource(topicsResource, '/topics/')

publisher_api.add_resource(pubTagRelationResource, '/pub_tag_relation/<int:relation_id>/')

publisher_api.add_resource(PubContractResource, '/contract/<int:contract_id>/')
publisher_api.add_resource(PubContractsResource, '/contracts/')