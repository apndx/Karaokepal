from application import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(1000), nullable=True)

    def __init__(self, name):
        self.name = name
