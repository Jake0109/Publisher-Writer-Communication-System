import uuid

from flask import request, g
from flask_restful import Resource, marshal, fields, abort, marshal_with

from App.APIs.utils import admin_login_required, publisher_login_required, publisherFields, multiPublisherFields
from App.Models.publisher.publisher_models import Publisher
from App.Models.publisher.publisher_tag_models import Publisher_Tag
from App.Models.writer.writer_models import Writer
from App.extensions import cache


class publisherResource(Resource):
    def get(self):
        publisher_id = request.args.get("id")
        publisher = Publisher.query.filter(Writer.is_deleted is False).get(publisher_id)

        print(publisher)
        print(type(publisher))
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
            publisher.password = request.form.get("password")
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

            publisher = Publisher.query.filter(Publisher.username == username).first()

            if not publisher or publisher.is_deleted:
                abort(404, msg="publisher does not exist")

            if not publisher.check_password(password):
                abort(400, msg="wrong username or password")

            token = "publisher" + uuid.uuid4().hex

            cache.set(token, publisher.id, timeout=60 * 60 * 24 * 7)
            id = cache.get(token)

            data = {
                "status": 200,
                "msg": "successfully login",
                "token": token,
                "data": marshal(publisher, publisherFields)
            }

            return data

    @publisher_login_required
    def patch(self):
        publisher = g.publisher
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
        tag_id = request.form.get("tag_id") or None
        if tag_id:
            relations = Publisher_Tag.query.filter(Publisher_Tag.tag_id == tag_id).all()

            if not relations:
                abort(400, msg="publisher-tag relationship not found")

            publisher_ids = [relation.publisher_id for relation in relations]
            publishers = [Publisher.query.get(publisher_id) for publisher_id in publisher_ids]

            data = {
                "msg": "publishers of certain tag successfully got",
                "status": 200,
                "data": publishers,
            }

            return data

        else:
            publishers = Publisher.query.filter(Publisher.is_deleted is False).all()

            data = {
                "msg": "publishers of certain tag successfully got",
                "status": 200,
                "data": publishers,
            }

            return data
