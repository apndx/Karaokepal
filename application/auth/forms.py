from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    
    class Meta:
        csrf = False


class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=5, max=144, message='The password should be longer than 4 and shorter than 144 characters')])
    username = StringField("Username", [validators.Length(min=5, max=30, message='The username should be longer than 5 and shorter than 30 characters')])
    password = PasswordField("Password", [validators.Length(min=4, max=30, message='The password should be longer than 4 and shorter than 30 characters')])
    
    class Meta:
        csrf = False        