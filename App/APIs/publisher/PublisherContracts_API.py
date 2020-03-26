from flask import g, request
from flask_restful import Resource, abort, marshal, marshal_with, reqparse

from App.APIs.utils import publisher_login_required, contractFields, multiContractFields
from App.Models.admin.contract_models import Contract

parse = reqparse.RequestParser()

class PubContractResource(Resource):
    @publisher_login_required
    def get(self):
        id = request.form.get("contract_id")
        contract = Contract.query.get(id)

        if not contract:
            abort(404, msg="contract not found.")

        if contract.publisher_id != g.publisher.id:
            abort(403, msg="permission refused.")

        data = {
            "msg": "contract successfully got",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data

    @publisher_login_required
    def post(self):
        contract = Contract()
        contract.name = request.form.get("name")
        contract.publisher_id = g.publisher.id
        contract.writer_id = request.form.get("writer_id")
        contract.contract_file = request.form.get("contract_file")

        if not contract.save():
            abort(400, msg="fail to save contract")

        data = {
            "msg": "contract successfully created",
            "status": 203,
            "data": contract
        }

        return data

    @publisher_login_required
    def patch(self):
        id = request.args.get("id")
        contract = Contract.query.get(id)

        if not contract:
            abort(404, msg="contract not found")

        contract.is_completed = True

        data = {
            "msg": "contract already completed",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data


class PubContractsResource(Resource):
    @publisher_login_required
    @marshal_with(multiContractFields)
    def get(self):

        contracts = Contract.query.filter(Contract.publisher_id == g.publisher.id).all()

        data = {
            "msg": "contracts of certain publisher successfully got.",
            "status": 200,
            "data": contracts
        }

        return data
