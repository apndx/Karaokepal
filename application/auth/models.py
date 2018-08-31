# application/auth/models.py

from application import db
from application.models import Base
from application.songs import models

# Database model for User 
class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)
    user_role = db.Column(db.String(20), nullable=False)

    def __init__(self, name, username, password, user_role):
        self.name = name
        self.username = username
        self.password = password
        self.user_role = user_role
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):

        if self.user_role == 'admin':
            return ["ADMIN"]
        else:
            return ["BASIC"]
 