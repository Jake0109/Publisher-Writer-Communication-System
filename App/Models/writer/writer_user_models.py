from werkzeug.security import check_password_hash, generate_password_hash

from App.Models import baseModel
from App.extensions import db


class Writer(baseModel):
    name = db.Column(db.String(32), nullable=False)
    _password = db.Column(db.String(64), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    tel = db.Column(db.String(32), nullable=False)
    mail = db.Column(db.String(64), nullable=False)

    @property
    def password(self):
        raise Exception("password cannot be accessed")

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self._password, pwd)