from flask import request, g
from flask_restful import Resource, marshal, abort, marshal_with, reqparse

from App.APIs.utils import publisher_login_required, topicField, multiTopicFields
from App.Models.publisher.topic_models import Topic

parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="please supply name")
parse.add_argument("writer_id", required=True, help="please supply writer_id")


class topicResource(Resource):
    def get(self, topic_id):
        topic = Topic.query.get(topic_id)

        if not topic or topic.is_deleted is True:
            abort(404, msg="topic not found")

        data = {
            "msg": "topic successfully get",
            "status": 200,
            "data": marshal(topic, topicField)
        }

        return data

    @publisher_login_required
    def patch(self, topic_id):

        topic = Topic.query.get(topic_id)

        if not topic or topic.is_deleted is True:
            abort(404, msg="topic not found")

        topic.is_approved = True

        if not topic.save():
            abort(400, msg="fail to save topic")

        if topic.publisher_id != g.publisher.id:
            abort(403, msg="forbidden")

        data = {
            "msg": "topic status successfully changed",
            "status": 200,
            "data": marshal(topic, topicField)
        }
        return data

    @publisher_login_required
    def delete(self, topic_id):
        topic = Topic.query.get(topic_id)

        if not topic:
            abort(404, msg="topic not found")

        if topic.publisher_id != g.publisher.id:
            abort(403, msg="forbidden")

        topic.is_deleted = True

        if not topic.save():
            abort(400, msg="fail to delete topic")

        return {"msg": "topic successfully deleted", "status": 200}


class topicsResource(Resource):
    @marshal_with(multiTopicFields)
    def get(self):
        writer_id = request.form.get("writer_id") or None
        if writer_id:
            topics = Topic.query.filter(Topic.writer_id == writer_id).all()
        else:
            topics = Topic.query.all()

        data = {
            "msg": "successfully get",
            "status": 200,
            "data": topics,
        }

        return data

    @publisher_login_required
    def post(self):
        topic = Topic()
        topic.publisher_id = g.publisher.id
        args = parse.parse_args()

        topic.writer_id = args.get("writer_id")
        topic.name = args.get("name")

        if not topic.save():
            abort(400, msg="fail to save topic")

        data = {
            "msg": "topic successfully created",
            "status": 201,
            "data": marshal(topic, topicField),
        }

        return data

