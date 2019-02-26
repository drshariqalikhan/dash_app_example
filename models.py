from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    # username = db.Column(db.String(80),unique = True)
    email = db.Column(db.String(120),unique = True)

    def __init__(self,email):
        # self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' %self.username