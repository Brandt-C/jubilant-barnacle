from requests import request
from app import app
from flask import render_template, request
from .forms import FindPoke
from .models import Pokedex

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find-poke', methods=['GET', 'POST'])
def find_poke():
    fp = FindPoke()
    dex = Pokedex()
    if request.method == 'POST':
        dex.add_poke(fp.data['poke_name'])
        return render_template('find-poke.html', fp=fp, dex=dex)
    return render_template('find-poke.html', fp=fp, dex=dex)
