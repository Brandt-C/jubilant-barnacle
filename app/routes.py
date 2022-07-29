from requests import request
from app import app
from flask import render_template, request
from .forms import FindPoke
from .models import Pokedex, Pokemon, db
from .services import choose4, funPhrase

@app.route('/')
def home():
    x = db.session.query(Pokemon.name).limit(15).all()
    rand_list = choose4(x)
    funp = funPhrase()
    randex = Pokedex()
    for r in rand_list:
        randex.add_poke(r)
    return render_template('index.html', randex=randex, funp=funp)

@app.route('/find-poke', methods=['GET', 'POST'])
def find_poke():
    fp = FindPoke()
    dex = Pokedex()
    if request.method == 'POST':
        dex.add_poke(fp.data['poke_name'])
        return render_template('find-poke.html', fp=fp, dex=dex)
    return render_template('find-poke.html', fp=fp, dex=dex)
