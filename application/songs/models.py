from application import db
from application.models import Base
from application.auth import models
from sqlalchemy.sql import text
from flask_login import login_required, current_user

accountsongs =  db.Table('accountsongs',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
)

artistsongs =  db.Table('artistsongs',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
)


class Song(Base):
    # parent left

    songname = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    users = db.relationship('User', secondary=accountsongs, backref=db.backref('songs', lazy=True))
    artists =  db.relationship('Artist', secondary=artistsongs, backref=db.backref('songs', lazy=True))

    def __init__(self, songname):
        self.songname = songname

    @staticmethod
    def find_songs_for_current_user():

        stmt = text("SELECT Song.songname, Song.description FROM Song"
                    " LEFT JOIN accountsongs ON Song.id = accountsongs.song_id"
                    " WHERE accountsongs.account_id = :cu").params(cu=current_user.id)            

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "description":row[1]})

        return response

    @staticmethod
    def how_many_have_this():

        stmt = text("SELECT Song.songname, COUNT(*) AS howmany FROM accountsongs, Song, Account"
                    " WHERE Song.id = accountsongs.song_id"
                    " AND Account.id = accountsongs.account_id"
                    " GROUP BY Song.songname"
                    )
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "howmany":row[1]})

        return response
