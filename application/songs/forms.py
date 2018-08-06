from flask_wtf import FlaskForm
from wtforms import StringField, validators

class SongForm(FlaskForm):
    name = StringField("Song name", [validators.Length(min=1)])
    description = StringField("Song description")
 
    class Meta:
        csrf = False
