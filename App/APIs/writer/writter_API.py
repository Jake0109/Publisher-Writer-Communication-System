import uuid
from flask import request, g
from flask_restful import Resource, marshal, fields, marshal_with, abort

from App.APIs.utils import get_writer_with_ident, writer_login_required, admin_login_required
from App.Models.writer.writer_models import Writer
from App.extensions import cache

writerFields = {
    "username": fields.String,
    "name": fields.String,
    "tel": fields.String,
    "mail": fields.String,
}

multiWriterFields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(writerFields)
}


class writerResource(Resource):
    @marshal_with(multiWriterFields)
    def get(self):
        writer_id = request.args.get(id)

        if not writer_id:
            abort(404, msg="invalid id")

        writer = get_writer_with_ident(writer_id)

        data = {
            "status": 200,
            "msg": "successfully get",
            "data": marshal(writer, writerFields)
        }

        return data

    def post(self):

        action = request.args.get("action")

        if action == "register":
            writer = Writer()
            writer.name = request.form.get("name")
            writer.password = request.form.get("password")
            writer.mail = request.form.get("mail")
            writer.tel = request.form.get("tel")

            if not writer.save():
                abort(400, msg="fail to save writer")

            data = {
                "msg": "successfully post",
                "status": 201,
                "data": marshal(writer, writerFields),
            }
            return data

        elif action == "login":

            ident = request.form.get("ident")
            password = request.form.get("password")

            writer = get_writer_with_ident(ident)

            if not writer:
                abort(400, msg="account does not exist")

            if not writer.check_password(password):
                abort(400, msg="wrong username or password")

            token = "writer"+uuid.uuid4().hex
            cache.set(token, writer.id, timeout=60 * 60 * 24 * 7)

            data = {
                "msg": "successfully login",
                "status": 200,
                "data": marshal(writer, writerFields),
                "token": token
            }

            return data

    @writer_login_required
    def patch(self):
        writer = g.writer
        writer.mail = request.form.get("mail") or writer.mail
        writer.tel = request.form.get("tel") or writer.tel

        if not writer.save():
            abort(400, msg="patch failed")

        data = {
            "msg": "successfully patched",
            "status": 200,
            "data": marshal(writer, writerFields)
        }

        return data

    @admin_login_required
    def delete(self):
        writer_id = request.args.get("id")
        writer = Writer.query.get(writer_id)
        writer.is_deleted = True

        return {"status": 203, "msg": "writer successfully deleted"}


class writersResource(Resource):
    def get(self):
        writers = Writer.query.filter(Writer.is_deleted == False).all()
        data = {
            "msg": "writer list fetched",
            "status": 200,
            "data": writers
        }

        return data
