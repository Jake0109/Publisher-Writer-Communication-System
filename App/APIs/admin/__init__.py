from flask_restful import Api

from App.APIs.admin.Contract_API import contractResource, contractsResource
from App.APIs.admin.admin_API import adminResource, adminsResource
from App.APIs.admin.tag_API import tagResource, tagsResource

admin_api = Api(prefix='/admin/')

admin_api.add_resource(adminResource, '/admin/<int:admin_id>/')
admin_api.add_resource(adminsResource, '/admins/')

admin_api.add_resource(contractResource, '/contract/<int:contract_id>/')
admin_api.add_resource(contractsResource, '/contracts/')

admin_api.add_resource(tagResource, '/tag/<int:tag_id>/')
admin_api.add_resource(tagsResource, '/tags/')