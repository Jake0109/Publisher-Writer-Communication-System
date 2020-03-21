from sqlalchemy import ForeignKey

from App.Models import baseModel
from App.Models.publisher.topic_models import Topic
from App.extensions import db


class Contract(baseModel):
    name = db.Column(db.String(128), nullable=False)
    t_id = db.Column(db.Integer, ForeignKey(Topic.id))
    contract_file = db.Column(db.String(256), nullable=False)
    is_signed = db.Column(db.Boolean, default=False)
    is_completed = db.Column(db.Boolean, default=False)
