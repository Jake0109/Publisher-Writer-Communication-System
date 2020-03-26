from flask import request, g
from flask_restful import abort, fields

from App.Models.admin.admin_models import Admin
from App.Models.publisher.publisher_models import Publisher
from App.Models.writer.writer_models import Writer
from App.extensions import cache


# writer utils

def get_writer_with_ident(ident):
    if not ident:
        return None

    writer = Writer.query.get(ident)
    if writer and not writer.is_deleted:
        return writer

    writer = Writer.query.filter(Writer.username == ident).first()
    if writer and not writer.is_deleted:
        return writer

    writer = Writer.query.filter(Writer.tel == ident).first()
    if writer and not writer.is_deleted:
        return writer

    writer = Writer.query.filter(Writer.mail == ident).first()
    if writer and not writer.is_deleted:
        return writer

    return None


def writer_login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        writer_id = cache.get(token)
        if not writer_id or not token.startswith('writer'):
            abort(400, msg="invalid token")

        g.writer = Writer.query.get(writer_id)

        return func(*args, **kwargs)

    return wrapper


# publisher utils

def publisher_login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        publisher_id = cache.get(token)

        if not publisher_id or not token.startswith("publisher"):
            abort(400, msg="invalid token")

        g.publisher = Publisher.query.get(publisher_id)

        return func(*args, **kwargs)

    return wrapper


# admin utils

def admin_login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        admin_id = cache.get(token)
        if not admin_id or not token.startwith("admin"):
            abort(400, msg="invalid token")

        g.admin = Admin.query.get(admin_id)

        return func(*args, **kwargs)

    return wrapper


def super_admin_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        admin_id = cache.get(token)
        if not admin_id or not token.startswith('admin'):
            abort(400, msg="invalid token")

        admin = Admin.query.get(admin_id)
        if not admin.is_super:
            abort(403, msg="invalid admin user")

        g.admin = admin

        return func(*args, **kwargs)

    return wrapper

# Fields
# Contract
contractFields = {
    "name": fields.String,
    "publisher_id": fields.Integer,
    "writer_id": fields.Integer,
    "contract_file": fields.String,
    "is_signed": fields.Boolean,
    "is_completed": fields.Boolean,
}

multiContractFields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(contractFields))
}

# Admin
adminFields = {
    "username": fields.String,
    "password": fields.String(attribute="_password"),
}

multiAdminFields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(adminFields))
}

# Tag
tagFields = {
    "id": fields.Integer,
    "name": fields.String
}

multiTagFields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(tagFields))
}

# Publisher
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

# Publisher-Tag Relation
relationFields = {
    "publisher_id": fields.Integer,
    "tag_id": fields.Integer,
}

multiRelationsFields = {
    "msg": fields.String,
    "status": fields.Integer,
    "data": fields.List(fields.Nested(relationFields))
}

# Topic
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

# Writer
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
