from flask import g
from flask_restful import Resource, abort, marshal, reqparse

from App.APIs.utils import publisher_login_required, relationFields
from App.Models.publisher.publisher_tag_models import Publisher_Tag

parse = reqparse.RequestParser()
parse.add_argument("tag_id", required=True, help="please supply tag_id")


class pubTagRelationResource(Resource):
    @publisher_login_required
    def post(self):
        relation = Publisher_Tag()
        args = parse.parse_args()

        relation.publisher_id = g.publisher.id
        relation.tag_id = args.get("tag_id")

        if not relation.save():
            abort(400, msg="fail to save publisher-tag relationship")

        data = {
            "msg": "publisher-tag relationship successfully created",
            "status": 200,
            "data": marshal(relation, relationFields)
        }

        return data

    @publisher_login_required
    def delete(self, relation_id):
        relation = Publisher_Tag.query.get(relation_id)

        if not relation:
            abort(404, msg="publisher-tag relationship not found")

        relation.delete()

        return {"msg": "publisher-tag relationship successfully deleted", "status": 200}
