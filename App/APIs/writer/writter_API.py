import uuid
from flask import request, g
from flask_restful import Resource, marshal, marshal_with, abort, reqparse

from App.APIs.utils import get_writer_with_ident, writer_login_required, admin_login_required, multiWriterFields, \
    writerFields
from App.Models.writer.writer_models import Writer
from App.extensions import cache

register_parse = reqparse.RequestParser()
register_parse.add_argument("name", required=True, help="please supply name")
register_parse.add_argument("username", required=True, help="please supply username")
register_parse.add_argument("password", required=True, help="please supply password")
register_parse.add_argument("mail", required=True, help="please supply mail")
register_parse.add_argument("tel", required=True, help="please supply telephone number")

login_Parse = reqparse.RequestParser()
login_Parse.add_argument("password", required=True, help="please supply password")
login_Parse.add_argument("ident")


class writerResource(Resource):
    def get(self, writer_id):
        writer = Writer.query.get(writer_id)

        if not writer:
            abort(404, msg="writer not found")

        data = {
            "status": 200,
            "msg": "successfully get",
            "data": marshal(writer, writerFields)
        }

        return data

    @admin_login_required
    def delete(self, writer_id):
        writer = Writer.query.get(writer_id)

        if not writer or writer.is_deleted is True:
            abort(404, msg="writer not found")

        writer.is_deleted = True

        if not writer.save():
            abort(400, msg="fail to delete writer")

        return {"status": 203, "msg": "writer successfully deleted"}


class writersResource(Resource):
    @marshal_with(multiWriterFields)
    def get(self):
        writers = Writer.query.filter(Writer.is_deleted == False).all()
        data = {
            "msg": "writer list fetched",
            "status": 200,
            "data": writers
        }

        return data

    def post(self):

        action = request.args.get("action")

        if action == "register":
            writer = Writer()
            args = register_parse.parse_args()

            writer.name = args.get("name")
            writer.username = args.get("username")
            writer.password = args.get("password")
            writer.mail = args.get("mail")
            writer.tel = args.get("tel")

            if not writer.save():
                abort(400, msg="fail to save writer")

            data = {
                "msg": "successfully post",
                "status": 201,
                "data": marshal(writer, writerFields),
            }
            return data

        elif action == "login":

            args = login_Parse.parse_args()

            ident = args.get("ident")
            password = request.form.get("password")

            writer = get_writer_with_ident(ident)

            if not writer:
                abort(400, msg="account does not exist")

            if not writer.check_password(password):
                abort(400, msg="wrong username or password")

            token = "writer" + uuid.uuid4().hex
            cache.set(token, writer.id, timeout=60 * 60 * 24 * 7)

            data = {
                "msg": "successfully login",
                "status": 200,
                "data": marshal(writer, writerFields),
                "token": token
            }

            return data

    @admin_login_required
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
