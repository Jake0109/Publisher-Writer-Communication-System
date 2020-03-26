from sqlalchemy import ForeignKey

from App.Models import baseModel
from App.Models.publisher.publisher_models import Publisher
from App.Models.writer.writer_models import Writer
from App.extensions import db


class Contract(baseModel):
    name = db.Column(db.String(128), nullable=False)
    publisher_id = db.Column(db.Integer, ForeignKey(Publisher.id))
    writer_id = db.Column(db.Integer, ForeignKey(Writer.id))
    contract_file = db.Column(db.String(256), nullable=False)
    is_signed = db.Column(db.Boolean, default=False)
    is_completed = db.Column(db.Boolean, default=False)
