from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    is_banned = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    is_verified = db.Column(db.Boolean, unique=False, nullable=False, default=True)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    projects = db.relationship('Project', backref='author', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False, default='Untitled')
    file_path = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.id
    
    



    