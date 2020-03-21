from flask import request
from flask_restful import Resource, marshal, fields, marshal_with

from App.Models.writer.writer_models import Writer

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

        writer = Writer()
        writer.name = request.form.get("name")
        writer.password = request.form.get("password")
        writer.mail = request.form.get("mail")
        writer.tel = request.form.get("tel")


        writer.save()

        data = {
            "msg": "successfully post",
            "status": 201,
            "data": marshal(writer, writerFields),
        }
        return data
