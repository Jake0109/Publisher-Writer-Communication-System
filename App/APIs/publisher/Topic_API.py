from flask import request, g
from flask_restful import Resource, marshal, fields, abort, marshal_with

from App.APIs.utils import admin_login_required, publisher_login_required
from App.Models.publisher.topic_models import Topic

topicField = {
    "name": fields.String,
    "writer_id": fields.Integer,
    "publisher_id": fields.Integer,
    "is_approved": fields.Boolean,
    "is_completed": fields.Boolean,
}

multiTopicFields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(topicField))
}

class topicResource(Resource):
    def get(self):
        topic_id = request.args.get("id")
        topic = Topic.query.get(topic_id)

        data = {
            "msg": "seccessfully get",
            "status": 200,
            "data": marshal(topic, topicField)
        }

        return data

    @publisher_login_required
    def post(self):
        topic = Topic()
        topic.publisher_id = g.publisher.id

        topic.writer_id = request.form.get("writer_id")
        topic.name = request.form.get("name")

        if not topic.save():
            abort(400, msg="fail to save topic")

        data = {
            "msg": "topic successfully created",
            "status": 203,
            "data": marshal(topic, topicField),
        }

        return data

    @admin_login_required
    def delete(self):
        topic_id = request.args.get("id")
        topic = Topic.query.get(topic_id)

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
