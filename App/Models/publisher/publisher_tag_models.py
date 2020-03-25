from App.Models import baseModel
from App.Models.admin.tag_models import Tag
from App.Models.publisher.publisher_models import Publisher
from App.extensions import db


class Publisher_Tag(baseModel):
    publisher_id = db.Column(db.Integer, db.ForeignKey(Publisher.id))
    tag_id = db.Column(db.Integer, db.ForeignKey(Tag.id))
