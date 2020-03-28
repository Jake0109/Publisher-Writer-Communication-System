from flask import g, request
from flask_restful import Resource, abort, marshal, marshal_with, reqparse

from App.APIs.utils import publisher_login_required, contractFields, multiContractFields
from App.Models.admin.contract_models import Contract
from App.settings import UPLOAD_DIR

parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="please supply name")
parse.add_argument("writer_id", required=True, help="please supply writer_id")


class PubContractResource(Resource):
    @publisher_login_required
    def get(self, contract_id):
        contract = Contract.query.get(contract_id)

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
        args = parse.parse_args()

        contract.name = args.get("name")
        contract.publisher_id = g.publisher.id
        contract.writer_id = args.get("writer_id")
        # contract.contract_file = request.file.get("contract_file")

        contract_file = args.get("contract_file")

        filepath = UPLOAD_DIR + contract_file.filename

        contract.contract_file = filepath

        if not contract.save():
            abort(400, msg="fail to save contract")

        data = {
            "msg": "contract successfully created",
            "status": 201,
            "data": contract
        }

        return data

    @publisher_login_required
    def patch(self, contract_id):
        contract = Contract.query.get(contract_id)

        if not contract:
            abort(404, msg="contract not found")

        if contract.publisher_id != g.publisher.id:
            abort(403, msg="Forbidden")

        contract.is_completed = True

        data = {
            "msg": "contract already completed",
            "status": 200,
            "data": marshal(contract, contractFields)
        }

        return data

    @publisher_login_required
    def delete(self, contract_id):
        contract = Contract.query.get(contract_id)

        if not contract:
            abort(404, msg="contract not found")

        if contract.publisher_id != g.publisher.id:
            abort(403, msg="Forbidden")

        contract.delete()

        return {"msg": "contract successfully deleted", "status": 200}


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
