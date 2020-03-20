from flask import request
from flask_restful import Resource, marshal, fields

from App.Models.writer.writer_user_models import Writer

writerFields = {
    "name": fields.String,
    "tel": fields.String,
    "mail": fields.String,
}


class writerResource(Resource):
    def get(self):
        data = {
            "msg": "user list fetched",
            "status": 200,
        }

        return data

    def post(self):

        writer = Writer()
        writer.name = request.form.get("name")
        writer.password = request.form.get("password")
        writer.mail = request.form.get("mail")
        writer.tel = request.form.get("tel")

        writer.save()

        data = {
            "msg": "successfully post",
            "status": 201,
            "data": None,
        }
        return data
