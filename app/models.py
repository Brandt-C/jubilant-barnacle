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
    # Taking these out to simplify the process here- might revisit this in future.
    # types = db.Column(db.String(255))
    # abilities = db.Column(db.String(255))
    # moves = db.Column(db.String(255))
    name = db.Column(db.String(50))
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    att = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    sprite = db.Column(db.String(255))
    shiny_sprite = db.Column(db.String(255))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    user = db.Column(db.String(50))

    def __init__(self, name, hp, defense, att, speed, sprite, shiny_sprite, height, weight, id):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.att = att
        self.speed = speed
        self.sprite = sprite
        self.shiny_sprite = shiny_sprite
        self.height = height
        self.weight = weight
        self.id = id

    def to_dict(self):
        return {
            'name' : self.name,
            'hp' : self.hp,
            'defense' : self.defense,
            'att' : self.att,
            'speed' : self.speed,
            'sprite' : self.sprite,
            'shiny_sprite' : self.shiny_sprite,
            'height': self.height,
            'weight' : self.weight,
            'id' : self.id
        }
    def disp_poke(self):
        print(f"\n{self.name.title()}- Weight- {self.weight} Height-{self.height} HP-{self.hp} Defense-{self.defense} Attack-{self.att}\n")
        print(f"\nSprite-{self.sprite},\n Shiny-{self.shiny_sprite}\n\n")

class Moves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    power = db.Column(db.Integer)
    pp = db.Column(db.Integer)

class Pokedex:
    def __init__(self):
        self.pokemon = {}
        
    def add_poke(self, pname):
        mempoke = Pokemon.query.filter(Pokemon.name==pname).first()
        if mempoke:
            print(mempoke, type(mempoke))
            data = mempoke.to_dict()
            hp = data['stats'][0]['base_stat']
            defense = data['stats'][2]['base_stat']
            att = data['stats'][1]['base_stat']
            speed = data['stats'][5]['base_stat']
            sprite = data['sprites']['front_default']
            shiny_sprite = data['sprites']['front_shiny']
            height = data['height']
            weight = data['weight']
            id = data['id']
            new_poke = Pokemon(pname, hp, defense, att, speed, sprite, shiny_sprite, height, weight, id)
            self.pokemon[pname] = new_poke
        else:
            result = r.get("https://pokeapi.co/api/v2/pokemon/" + pname.lower())
            data = result.json()
            hp = data['stats'][0]['base_stat']
            defense = data['stats'][2]['base_stat']
            att = data['stats'][1]['base_stat']
            speed = data['stats'][5]['base_stat']
            sprite = data['sprites']['front_default']
            shiny_sprite = data['sprites']['front_shiny']
            height = data['height']
            weight = data['weight']
            id = data['id']
            
            new_poke = Pokemon(pname, hp, defense, att, speed, sprite, shiny_sprite, height, weight, id)
            db.session.add(new_poke)
            db.session.commit()
                        #Taking these out to simplify for now- may revisit later
            # for a in data['abilities']:
            #     new_poke.abilities.append(a['ability']['name'])
            # for b in data['types']:
            #     new_poke.types.append(b['type']['name'])
            # for c in data['moves']:
            #     new_poke.moves.append(c['move']['name'])
            # for x in range(3,len(new_poke.moves)):
            #     new_poke.moves.pop()
            self.pokemon[pname] = new_poke
            
        
    def show_dex(self):
        for n in self.pokemon:
            self.pokemon[n].disp_poke()