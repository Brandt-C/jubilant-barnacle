from requests import request
from app import app
from flask import render_template, request
from .forms import FindPoke

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find-poke', methods=['GET', 'POST'])
def find_poke():
    # fp = FindPoke()
    # if request.method == 'POST':
    #     fp.data
    return render_template('find-poke.html')
