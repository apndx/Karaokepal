# application/songs/models.py

import os
from application import db
from application.models import Base
from application.auth import models
from sqlalchemy.sql import text
from flask_login import login_required, current_user

artistsongs =  db.Table('artistsongs',
    db.Column('song_id', db.Integer, db.ForeignKey('song.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
)


class Song(Base):
    # parent left

    songname = db.Column(db.String(144), nullable=False, index=True)
    description = db.Column(db.String(1000), nullable=True)

    users = db.relationship('Accountsongs', cascade='delete', lazy=True)
    artists =  db.relationship('Artist', secondary=artistsongs, backref=db.backref('songs', lazy=True))

    def __init__(self, songname):
        self.songname = songname

    # Finds the songs the current user has chosen, the list is sorted by what has been sung most
    @staticmethod
    def find_songs_for_current_user():
        
        stmt = text("SELECT Song.id, Song.songname, Accountsongs.count, Song.description FROM Song, Accountsongs"
                    " WHERE Song.id = Accountsongs.song_id"
                    " AND Accountsongs.account_id = :cu"
                    " ORDER BY Accountsongs.count DESC").params(cu=current_user.id) 

        res = db.engine.execute(stmt)

        response = []
        for row in res:

            response.append({"id":row[0], "name":row[1], "count":row[2], "description":row[3]})

        return response

    @staticmethod
    def how_many_have_this():

        if os.environ.get("HEROKU"):
        
            stmt = text("SELECT Song.songname, COUNT(accountsongs.song_id) AS howmany FROM Song "
                        " LEFT JOIN accountsongs ON Song.id = accountsongs.song_id "
                        " LEFT JOIN Account ON Account.id = accountsongs.account_id "
                        " GROUP BY Song.id  ORDER BY howmany DESC ")

            res = db.engine.execute(stmt)
            response = []
            for row in res:
                response.append({"name":row[0], "howmany":row[1]})

        else:    

            stmt = text("SELECT Song.songname, Artist.artistname, COUNT(DISTINCT account.id) FROM Song"
                            " LEFT JOIN Accountsongs ON Song.id = accountsongs.song_id "
                            " LEFT JOIN artistsongs ON artistsongs.song_id = Song.id"
                            " LEFT JOIN Artist ON Artist.id = artistsongs.artist_id"
                            " LEFT JOIN Account ON Account.id = accountsongs.account_id "
                            " GROUP BY Song.id ORDER BY COUNT(DISTINCT account.id) DESC ")

            res = db.engine.execute(stmt)
            response = []
            for row in res:
                response.append({"name":row[0], "artist":row[1], "howmany":row[2]})

        return response

    @staticmethod
    def find_artist_for_song(song):        

        stmt = text("SELECT Artist.id FROM Artist"
                    " LEFT JOIN artistsongs ON Artist.id = artistsongs.artist_id "
                    " LEFT JOIN Song ON Song.id = artistsongs.song_id"
                    " WHERE Song.id = :cs").params(cs=song.id)

        res = db.engine.execute(stmt)

        response = res.fetchone()[0]
      
        return response

    @staticmethod
    def list_songs_with_artistname():

        stmt = text("SELECT Song.id, Song.songname, Artist.artistname FROM Song"
                    " LEFT JOIN artistsongs ON Song.id = artistsongs.song_id "
                    " LEFT JOIN Artist ON Artist.id = artistsongs.artist_id"
                    " ORDER BY Song.songname")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "songname":row[1], "artistname":row[2]})

        return response            

    @staticmethod
    def check_artistsong(song, artist):          
        stmt = text("SELECT * FROM artistsongs"
                     " WHERE artistsongs.artist_id = :ai"
                     " AND artistsongs.song_id = :si").params(ai=artist.id, si=song.id)

        res = db.engine.execute(stmt)

        response = res.fetchone()
        
        if response==None:
            return False
        else: 
            return True 

    # this method is for adding a new song to the database
    @staticmethod
    def new_song_dbs(song, artist):
        db.session().add(song)
        db.session().commit()
        db.session().add(artist)
        db.session().commit()    
        song.artists.append(artist) # attach artist and song
        db.session().commit()

class Accountsongs(db.Model):
    
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), primary_key=True,
        nullable=False)

    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True,
        nullable=False)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    modulation = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    owndescription = db.Column(db.String(1000), nullable=True)

    def __init__(self, account, song, modulation, count):
       self.account_id = account.id
       self.song_id = song.id 
       self.modulation = 0 # this tells if this song should be modulated (if the key is too high or low)
       self.count = 0 # this tells how many times a user has sung this song

    # For validating if this accountsong already exists
    @staticmethod
    def check_if_exists(song, user):   

        stmt = text("SELECT * FROM Accountsongs"
                     " WHERE accountsongs.account_id = :ai"
                     " AND accountsongs.song_id = :si").params(ai=user.id, si=song.id)

        res = db.engine.execute(stmt)

        response = res.fetchone()
        
        if response==None:
            return False
        else: 
            return True          

