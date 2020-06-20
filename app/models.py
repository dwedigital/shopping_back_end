from app import db


class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(128), index=True, unique=False)
    quantity = db.Column(db.Integer(), index=False, unique=False)
    status = db.Column(db.Boolean, default=False,nullable=False)

