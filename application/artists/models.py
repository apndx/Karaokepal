from application import db
from application.models import Base
from application.songs import models


class Artist(Base):

    artistname = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    
    def __init__(self, artistname):
        self.artistname = artistname