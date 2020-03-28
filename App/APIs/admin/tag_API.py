from flask import request
from flask_restful import Resource, abort, marshal, marshal_with, reqparse

from App.APIs.utils import admin_login_required, tagFields, multiTagFields
from App.Models.admin.tag_models import Tag
from App.Models.publisher.publisher_tag_models import Publisher_Tag

parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="please supply name")


class tagResource(Resource):

    @admin_login_required
    def delete(self, tag_id):
        tag = Tag.query.get(tag_id)

        if not tag.delete():
            abort(400, msg="fail to delete tag")

        return {"msg": "tag successfully deleted", "status": 203}


class tagsResource(Resource):
    @marshal_with(multiTagFields)
    def get(self):
        publisher_id = request.form.get("publisher_id") or None
        if not publisher_id:
            tags = Tag.query.all()

            data = {
                "msg": "tags successfully got",
                "status": 200,
                "data": tags
            }

            return data

        else:
            relations = Publisher_Tag.query.filter(Publisher_Tag.publisher_id == publisher_id).all()

            if not relations:
                abort(400, msg="publisher-tag relationship not found")

            tag_ids = [relation.tag_id for relation in relations]
            tags = [Tag.query.get(tag_id) for tag_id in tag_ids]

            data = {
                "msg": "tags of certain publisher successfully got",
                "status": 200,
                "data": tags
            }

            return data

    @admin_login_required
    def post(self):
        tag = Tag()
        args = parse.parse_args()

        tag.name = args.get("name")

        if not tag.save():
            abort(400, msg="fail to save tag")

        data = {
            "msg": "tag successfully created",
            "status": 201,
            "data": marshal(tag, tagFields)
        }

        return data
