from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.Length(min=1, max=144)])
    description = StringField("Song description", [validators.Length(max=999)])
 
    class Meta:
        csrf = False
