import requests as r
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4

from flask_login import LoginManager, UserMixin

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, first_name= "", last_name = ""):
        self.username =username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password)
        self.id = str(uuid4())

class Pokemon(db.Model):  
    id = db.Column(db.Integer, primary_key=True)
    types = db.Column(db.String(255))
    abilities = db.Column(db.String(255))
    moves = db.Column(db.String(255))
    name = db.Column(db.String(50))
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    att = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    sprite = db.Column(db.String(255))
    shiny_sprite = db.Column(db.String(255))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)



    # self.types = []
    # self.abilities = []
    # self.moves = []
    # self.name = name
    # self.hp = hp
    # self.defense = defense
    # self.att = att
    # self.speed = speed
    # self.sprite = sprite
    # self.shiny_sprite = shiny_sprite
    # self.height = height
    # self.weight = weight
    # self.id = id

