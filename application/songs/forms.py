from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SongForm(FlaskForm):
    songname = StringField("Song name", [validators.Length(min=1, max=144)])
    description = StringField("Song description", [validators.Length(max=999)])
    artistname = StringField("Artist", [validators.Length(min=1, max=144)])
 
    class Meta:
        csrf = False
