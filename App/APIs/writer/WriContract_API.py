from flask_restful import Resource

from App.APIs.utils import writer_login_required


class WriContractResource(Resource):
    @writer_login_required
    def get(self):
        # permission_required()
        pass

    @writer_login_required
    def patch(self):
        pass


class WriContractsResource(Resource):
    @writer_login_required
    def get(self):
        pass
