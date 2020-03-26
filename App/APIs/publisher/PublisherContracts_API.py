from flask import g, request
from flask_restful import Resource, abort, marshal, marshal_with

from App.APIs.utils import publisher_login_required, contractFields, multiContractFields
from App.Models.admin.contract_models import Contract
from App.Models.publisher.topic_models import Topic


class PubContractResource(Resource):
    @publisher_login_required
    def get(self):
        publisher_id = g.publisher.id
        contract_id = request.args.get("contract_id")
        contract = Contract.query.get(contract_id)
        topic = Topic.query.get(contract.t_id)

        if not topic.publisher_id == publisher_id:
            abort(403, msg="it is not your contract.")

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
        contract.t_id = request.form.get("t_id")
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
        publisher_id = g.publisher.id
        topics = Topic.query.filter(Topic.publisher_id == publisher_id).all()
        topic_ids = [topic.id for topic in topics]
        contracts = [Contract.query.filter(topic_id).first() for topic_id in topic_ids]

        data = {
            "msg": "contracts of certain publisher successfully got.",
            "status": 200,
            "data": contracts
        }

        return data
