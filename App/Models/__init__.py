from App.extensions import db


class baseModel(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __extract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()