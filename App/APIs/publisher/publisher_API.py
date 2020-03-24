import uuid

from flask import request
from flask_restful import Resource, marshal, fields, abort, marshal_with

from App.APIs.utils import admin_login_required, publisher_login_required
from App.Models.publisher.publisher_models import Publisher
from App.Models.writer.writer_models import Writer
from App.extensions import cache

publisherFields = {
    "username": fields.String,
    "name": fields.String,
    "identifier": fields.String,
    "tel": fields.String,
    "address": fields.String,
}

multiPublisherFields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(publisherFields))
}


class publisherResource(Resource):
    def get(self):
        publisher_id = request.args.get("writer_id")
        publisher = Publisher.query.filter(Writer.is_deleted == False).get(publisher_id)

        if not publisher:
            abort(404, msg="invalid publisher's id")
        data = {
            "status": 200,
            "msg": "successfully get writer",
            "data": marshal(publisher, publisherFields)
        }

        return data

    def post(self):
        action = request.args.get("action")

        if action == "register":
            publisher = Publisher()
            publisher.username = request.form.get("username")
            publisher.name = request.form.get("name")
            publisher.identifier = request.form.get("identifier")
            publisher.tel = request.form.get("name")
            publisher.mail = request.form.get("mail")
            publisher.address = request.form.get("name")

            if not publisher.save():
                abort(400, msg="fail to save publisher")

            data = {
                "status": 200,
                "msg": "successfully saved publisher",
                "data": marshal(publisher, publisherFields)
            }

            return data

        elif action == "login":
            username = request.form.get("username")
            password = request.form.get("password")

            publisher = Publisher.qeury.filter(Publisher.username == username).first()

            if not publisher or publisher.is_deleted:
                abort(404, msg="publisher does not exist")

            if not publisher.check_password(password):
                abort(400, msg="wrong username or password")

            token = "publisher" + uuid.uuid4().hex

            cache.set(token, publisher.id, timeout=60 * 60 * 24 * 7)

            data = {
                "status": 200,
                "msg": "successfully login",
                "token": token,
                "data": marshal(publisher, publisherFields)
            }

            return data

    @publisher_login_required
    def patch(self):
        publisher_id = request.args.get("id")
        publisher = Publisher.query.get(Publisher.id == publisher_id)
        publisher.identifier = request.form.get("identifier") or publisher.identifier
        publisher.tel = request.form.get("name") or publisher.tel
        publisher.mail = request.form.get("mail") or publisher.mail
        publisher.address = request.form.get("name") or publisher.address

        if not publisher.save():
            abort(400, msg="patch failed")

        data = {
            "msg": "successfully patched",
            "status": 200,
            "data": marshal(publisher, publisherFields)
        }

        return data

    @admin_login_required
    def delete(self):
        publisher_id = request.args.get("id")
        publisher = Publisher.query.get(publisher_id)

        if not publisher:
            abort(404, msg="publisher not found")

        publisher.is_deleted = True

        return {"status": 203, "msg": "publisher successfully deleted"}


class publishersResource(Resource):
    @marshal_with(multiPublisherFields)
    def get(self):
        # not include tags

        publishers = Publisher.query.filter(Publisher.is_deleted == False).all()
        return publishers
