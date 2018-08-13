from application import db
from application.models import Base
from application.auth import models

accountsongs =  db.Table('accountsongs',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

class Song(Base):
    # parent left

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    users = db.relationship('User', secondary=accountsongs, backref=db.backref('songs', lazy=True))

    def __init__(self, name):
        self.name = name
