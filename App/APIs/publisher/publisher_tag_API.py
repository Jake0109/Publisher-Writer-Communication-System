from flask import g, request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.APIs.utils import publisher_login_required, relationFields, multiRelationsFields
from App.Models.admin.tag_models import Tag
from App.Models.publisher.publisher_models import Publisher
from App.Models.publisher.publisher_tag_models import Publisher_Tag


class pubTagRelationResource(Resource):
    @publisher_login_required
    def post(self):
        relation = Publisher_Tag()
        relation.publisher_id = g.publisher.id
        relation.tag_id = request.form.get("tag_id")

        if not relation.save():
            abort(400, msg="fail to save publisher-tag relationship")

        data = {
            "msg": "publisher-tag relationship successfully created",
            "status": 200,
            "data": marshal(relation, relationFields)
        }

        return data


    @publisher_login_required
    def delete(self):
        id = request.form.get("id")
        relation = Publisher_Tag.query.get(id)

        if not relation:
            abort(404, msg="publisher-tag relationship not found")

        return {"msg": "publisher-tag relationship successfully deleted", "status": 200}


class pubTagRelationsResource(Resource):
    @marshal_with(multiRelationsFields)
    def get(self):
        publisher_id = request.form.get("publisher_id") or None
        tag_id = request.form.get("tag_id") or None
        if publisher_id and tag_id:
            abort(400, msg="invalid request")

        elif not publisher_id and not tag_id:
            relations = Publisher_Tag.query.all()

            data = {
                "msg": "relations successfully got",
                "status": 200,
                "data": relations
            }
            return data

        elif publisher_id:
            publisher = Publisher.query.get(publisher_id)
            if not publisher:
                abort(404, msg="publisher not found")

            relations = Publisher_Tag.query.filter(Publisher_Tag.publisher_id == publisher_id)

            data = {
                "msg": "relationships of certain publisher successfully got",
                "status": 200,
                "data": relations,
            }

            return data

        else:
            tag = Tag.query.get(tag_id)
            if not tag:
                abort(404, msg="tag not found")

            relations = Publisher_Tag.query.filter(Publisher_Tag.tag_id == tag_id)

            data = {
                "msg": "relationships of certain tag successfully got",
                "status": 200,
                "data": relations,
            }

            return data