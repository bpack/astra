import datetime
from astra import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User '{}'>".format(self.username)

    def map(self):
        return { 'id': self.id, 'username': self.username, 'email': self.email}


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(2000))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    done = db.Column(db.Boolean)
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<Task {}: {}>".format(self.id, self.title)

    def map(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created': self.created_date,
            'done': self.done
        }
    
