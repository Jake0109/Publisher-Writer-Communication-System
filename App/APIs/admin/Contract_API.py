from flask import request
from flask_restful import Resource, abort, marshal, marshal_with

from App.APIs.utils import admin_login_required, contractFields, multiContractFields
from App.Models.admin.contract_models import Contract


class contractResource(Resource):
    @admin_login_required
    def get(self, contract_id):
        contract = Contract.query.get(contract_id)

        if not contract:
            abort(404, msg="contract not found.")

        data = {
            "msg": "contract successfully got.",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data


class contractsResource(Resource):
    @admin_login_required
    @marshal_with(multiContractFields)
    def get(self):
        contracts = Contract.query.all()

        data = {
            "msg": "contracts successfully got.",
            "status": 200,
            "data": contracts
        }

        return data
