# application/songs/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, validators


class SongForm(FlaskForm):
    songname = StringField("Song name", [validators.Length(min=1, max=144, message=('1-144 characters'))])
    description = StringField("Song description", [validators.Length(max=999)])
    artistname = StringField("Artist", [validators.Length(min=1, max=144, message=('1-144 characters'))])
 
    class Meta:
        csrf = False

class ChangeSongForm(FlaskForm):
    songname = StringField("Song name", [validators.Length(min=1, max=144, message=('1-144 characters'))])
    description = StringField("Song description", [validators.Length(max=999)])
    
    class Meta:
        csrf = False