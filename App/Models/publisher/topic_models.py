from sqlalchemy import ForeignKey

from App.Models import baseModel
from App.Models.admin.admin_models import Admin
from App.Models.writer.writer_models import Writer
from App.extensions import db


class Topic(baseModel):
    name = db.Column(db.String(256), nullable=False)
    p_id = db.Column(db.Integer, ForeignKey(Admin.id))
    w_id = db.Column(db.Integer, ForeignKey(Writer.id))
    date = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)
    is_approved = db.Column(db.Boolean, default=False)
    is_completed = db.Column(db.Boolean, default=False)
