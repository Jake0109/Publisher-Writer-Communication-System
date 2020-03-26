from flask import request, g
from flask_restful import Resource, abort, marshal, marshal_with

from App.APIs.utils import writer_login_required, contractFields, multiContractFields
from App.Models.admin.contract_models import Contract


class WriContractResource(Resource):
    @writer_login_required
    def get(self):
        id = request.args.get("contract_id")
        contract = Contract.query.get(id)

        if not contract:
            abort(404, msg="contract not found.")

        if contract.id != g.wriiter.id:
            abort(403, msg="permission refused.")

        data = {
            "msg": "contract successfully got.",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data

    @writer_login_required
    def patch(self):
        id = request.args.get("contract_id")
        contract = Contract.query.get(id)

        if not contract:
            abort(404, msg="contract not found.")

        if contract.id != g.wriiter.id:
            abort(403, msg="permission refused.")

        contract.is_signed = True

        if not contract.save():
            abort(400, msg="fail to save contract")

        data = {
            "msg": "contract successfully changed.",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data


class WriContractsResource(Resource):
    @writer_login_required
    @marshal_with(multiContractFields)
    def get(self):
        contracts = Contract.query.filter(Contract.writer_id == g.writer.id).all()

        data = {
            "msg": "contracts of certain writer successfully got.",
            "status": 200,
            "data": contracts
        }

        return data
