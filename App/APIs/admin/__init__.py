from flask_restful import Api

from App.APIs.admin.Contract_API import contractResource, contractsResource
from App.APIs.admin.admin_API import adminResource
from App.APIs.admin.tag_API import tagResource, tagsResource

admin_api = Api(prefix='/admin/')

admin_api.add_resource(adminResource, '/admin/')

admin_api.add_resource(contractResource, '/contract/')
admin_api.add_resource(contractsResource, '/contracts')

admin_api.add_resource(tagResource, '/tag/')
admin_api.add_resource(tagsResource, '/tags/')