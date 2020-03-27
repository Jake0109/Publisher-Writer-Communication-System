import uuid

from flask import request, g
from flask_restful import Resource, abort, marshal, marshal_with, reqparse

from App.APIs.utils import admin_login_required, super_admin_required, adminFields, multiAdminFields
from App.Models.admin.admin_models import Admin
from App.extensions import cache
from App.settings import SUPER_ADMINS

parse = reqparse.RequestParser()
parse.add_argument("username", required=True, help="please supply username")
parse.add_argument("password", required=True, help="please supply password")

class adminResource(Resource):
    def get(self):
        admin_id = request.args.get("id")
        admin = Admin.query.get(admin_id)

        if not admin:
            abort(404, msg="admin not found")

        data = {
            "msg": "admin successfully got",
            "status": 200,
            "data": marshal(admin, adminFields),
        }

        return data

    def post(self):
        action = request.args.get("action")
        args = parse.parse_args()

        if action == "register":
            admin = Admin()

            admin.username = args.get("username")
            admin.password = args.get("password")

            if not admin.save():
                abort(400, msg="fail to save admin")

            data = {
                "msg": "admin successfully created",
                "status": 201,
                "data": marshal(admin, adminFields),
            }

            return data

        elif action == "login":
            username = args.get("username")
            password = args.get("password")

            admin = Admin.query.filter(Admin.username == username).first()
            if not admin:
                abort(404, msg="admin not found")

            if not admin.check_password(password):
                abort(400, msg="invalid username or password")

            if username in SUPER_ADMINS:
                admin.is_super = True

            token = "admin" + uuid.uuid4().hex
            cache.set(token, admin.id, timeout=60 * 60 * 24 * 7)

            data = {
                "msg": "successfully login",
                "status": 200,
                "token": token,
                "data": marshal(admin, adminFields)
            }

            return data

    @admin_login_required
    def patch(self):
        admin = g.admin

        args = parse.parse_args()
        password = args.get("password")

        admin.password = password

        if not admin.save():
            abort(400, msg="fail to patch")

        data = {
            "msg": "successfully changed",
            "status": 200,
            "data": marshal(admin, adminFields)
        }

        return data

    @super_admin_required
    def delete(self):
        admin_id = request.args.get("id")
        admin = Admin.query.get(admin_id)

        if not admin:
            abort(404, msg="admin not found")

        admin.is_deleted = True

        return {"msg": "successfully deleted", "status": 200}

class AdminsResource(Resource):
    @super_admin_required
    @marshal_with(multiAdminFields)
    def get(self):
        admins = Admin.query.all()

        data = {
            "msg": "admins successfully get",
            "status": 200,
            "data": admins
        }

        return data
