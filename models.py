from app import db
from sqlalchemy.dialects.postgresql import JSON

class FluDb(db.metadata):
    __tablename__ = "News"

    id = db.Column(db.Integer,primary_key = True)
    news = db.Column(JSON)

    def __init__(self,news):
        self.news = news
    
    def __repr__(self):
        return '<news %r>' %self.news