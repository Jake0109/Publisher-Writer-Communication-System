from flask import request, g
from flask_restful import abort

from App.Models.writer.writer_models import Writer
from App.extensions import cache


def get_writer(ident):

    if not ident:
        return None

    writer = Writer.query.get(ident)
    if writer:
        return writer

    writer = Writer.query.filter(Writer.name == ident).first()
    if writer:
        return writer

    writer = Writer.query.filter(Writer.tel == ident).first()
    if writer:
        return writer

    writer = Writer.query.filter(Writer.mail == ident).first()
    if writer:
        return writer

    return None

def writer_login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        writer_id = cache.get(token)
        if not writer_id:
            abort(400, msg="invalid token")

        g.writer = Writer.query.get(writer_id)

        return func(*args, **kwargs)
    return wrapper
