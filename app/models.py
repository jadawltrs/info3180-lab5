# Add any model classes for Flask-SQLAlchemy here

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(150), nullable=False)  # Store the filename of the uploaded poster
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster

