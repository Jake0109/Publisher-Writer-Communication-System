from flask import request, g
from flask_restful import abort

from App.Models.admin.admin_models import Admin
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
        if not writer_id or not token.startwith('writer'):
            abort(400, msg="invalid token")

        g.writer = Writer.query.get(writer_id)

        return func(*args, **kwargs)

    return wrapper


# admin utils
def admin_login_required(func):
    def wrapper(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            abort(400, msg="not login")

        admin_id = cache.get(token)
        if not admin_id or not token.startwith('admin'):
            abort(400, msg="invalid token")

        g.admin = Admin.query.get(admin_id)

        return func(*args, **kwargs)

    return wrapper
