from werkzeug.security import generate_password_hash, check_password_hash

from App.Models import baseModel
from App.extensions import db


class Publisher(baseModel):
    name = db.Column(db.String(128), nullable=False, unique=True)
    identifier = db.Column(db.String(256), nullable=False, unique=True)
    tel = db.Column(db.String(128), nullable=False, unique=True)
    address = db.Column(db.String(256), nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception("password not access")

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)
