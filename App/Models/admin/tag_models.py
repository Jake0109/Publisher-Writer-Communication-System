from App.Models import baseModel
from App.extensions import db


class Tag(baseModel):
    name = db.Column(db.String(64), nullable=True, unique=True)