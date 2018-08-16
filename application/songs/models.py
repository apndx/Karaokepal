from application import db
from application.models import Base
from application.auth import models
from sqlalchemy.sql import text
from flask_login import login_required, current_user

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

    @staticmethod
    def find_songs_for_current_user():

        stmt = text("SELECT Song.name, Song.description FROM Song"
                    " LEFT JOIN accountsongs ON Song.id = accountsongs.song_id"
                    " WHERE accountsongs.account_id = :cu").params(cu=current_user.id)            

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "description":row[1]})

        return response

    @staticmethod
    def how_many_have_this():

        stmt = text("SELECT Song.name, COUNT(*) AS howmany FROM accountsongs, Song, Account"
                    " WHERE Song.id = accountsongs.song_id"
                    " AND Account.id = accountsongs.account_id"
                    " GROUP BY Song.name"
                    )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "howmany":row[1]})

        return response
