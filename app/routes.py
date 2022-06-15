from app import app
from flask import render_template


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find-poke')
def find_poke():
    return render_template('find-poke.html')
