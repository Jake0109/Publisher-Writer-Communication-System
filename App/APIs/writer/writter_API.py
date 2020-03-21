import uuid

from flask import request
from flask_restful import Resource, marshal, fields, marshal_with, abort

from App.APIs.writer.utils import get_writer, writer_login_required
from App.Models.writer.writer_models import Writer
from App.extensions import cache

writerFields = {
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
        writers = Writer.query.all()
        print(writers)
        print(type(writers))
        data = {
            "msg": "user list fetched",
            "status": 200,
            "data": writers
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
                abort(400, msg="writer cannot be saved")

            data = {
                "msg": "successfully post",
                "status": 201,
                "data": marshal(writer, writerFields),
            }
            return data

        elif action == "login":
            pass
            ident = request.form.get("ident")
            password = request.form.get("password")

            writer = get_writer(ident)

            if not writer:
                abort(400, msg="account does not exist")

            if not writer.check_password(password):
                abort(400, msg="wrong username or password")

            token = uuid.uuid4().hex
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
        pass
        return {"msg": "patch ok"}
