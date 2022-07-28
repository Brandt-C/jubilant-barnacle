from requests import request
from flask import Blueprint, render_template, redirect, url_for, flash, request
user = Blueprint('user', __name__, template_folder='usertemplates', url_prefix='/user')

from .userforms import SignInForm, RegForm, FindPokeForm, BattleForm
from app.models import Pokemon, User, db, Pokedex, Battle
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, login_required, logout_user


@user.route('/', methods=['GET', 'POST'])
def signin():
    sform = SignInForm()
    if request.method == 'POST':
        if sform.validate_on_submit():
            user = User.query.filter_by(username=sform.username.data).first()
            if user and check_password_hash(user.password, sform.password.data):
                login_user(user)
                flash(f'Welcome back {sform.username.data}!', category='success')
                return redirect(url_for('user.userHome'))
        flash(f"Wrong Username or password.")
        return redirect(url_for('user.signin'))
    return render_template('signin.html', sform=sform)

@user.route('/register', methods=['GET', 'POST'])
def register():
    rform = RegForm()
    if request.method == 'POST':
        if rform.validate_on_submit():
            newuser = User(rform.username.data, rform.email.data, rform.password.data, rform.first_name.data, rform.last_name.data)
            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash(f'Username or email has been used previously, please try a different entry!')
                return redirect(url_for('user.register'))
            login_user(newuser)
            flash(f'Registration successful! Welcome {rform.first_name._value()}!', category='success')
            return redirect(url_for('user.userHome'))
        else:
            flash("didn't work!!!!!", category='danger')
            return redirect(url_for('user.register'))
    return render_template('register.html', rform=rform)

@user.route('/logout')
@login_required
def signOut():
    logout_user()
    flash('You have been logged out, please sign back in to access all the fun stuff!', category='warning')
    return redirect(url_for('user.signin'))

@user.route('/userhome', methods=['GET', 'POST'])
@login_required
def userHome():
    fpform = FindPokeForm()
    # catch = Catch()
    dex = Pokedex()
    mydex = Pokedex()
    my_dict = current_user.poke_dict()
    for x in my_dict.values():
        if x:
            mydex.add_poke(x)
    if request.method == "POST":
        if request.form.get('catch-btn') == 'catch':
                pname = request.form.get('name-catch')
                if pname not in my_dict:
                    current_user.add_poke(pname)
                    upoke = Pokemon.query.filter(Pokemon.name==pname).first()
                    upoke.catch(current_user.username)
                    flash(f'{pname} caught!', category='success')
                    return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)
                else:
                    flash(f'{pname} already caught!', category='danger')
                    return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)
        
        if request.form.get('release-btn') == 'release':
                pname = request.form.get('name-release')
                current_user.rem_poke(pname)
                upoke = Pokemon.query.filter(Pokemon.name==pname).first()
                upoke.release()
                flash(f'{pname} released!', category='warning')
                return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)

        if fpform.data:
            try:
                dex.add_poke(fpform.data['poke'])
                return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)
            except:
                flash(f'Poke not found, try again!', category='danger')
                return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)
  
    flash('Welcome back!', category='success')
    return render_template('userhome.html', my_dict=my_dict, dex=dex, fpform=fpform, mydex=mydex)

@user.route('/battle', methods=['GET', 'POST'])
@login_required
def battle():
    bform = BattleForm()
    ulist1 = db.session.query(User.username).all()
    ulist = list(map(lambda x: str(x)[2:-3], ulist1))
    cuserdex = Pokedex()
    oppuserdex = Pokedex()
    un = current_user.username
    my_dict = current_user.poke_dict()
    oppname = None
    for x in my_dict.values():
        if x:
            cuserdex.add_poke(x)
    print(oppname)
    if request.method == "POST":
        if request.form.get('catch-btn'):
            oppname = request.form.get('catch-btn')
            opp_user = User.query.filter(User.username==oppname).first()
            opp_pokes = opp_user.poke_dict()
            print(opp_pokes, oppname, opp_user)
            for x in opp_pokes.values():
                if x:
                    oppuserdex.add_poke(x)
            return render_template('battle.html', ulist=ulist, cuserdex=cuserdex, oppuserdex=oppuserdex, oppname=oppname, bform=bform, opp_user=opp_user)
            
        if bform.data:
            print(f'\nBform data-\t{bform.data}')
            oppname = bform.data['opp']
            opp_user = User.query.filter(User.username==oppname).first()
            opp_dict = opp_user.poke_dict()
            for x in opp_dict.values():
                if x:
                    oppuserdex.add_poke(x)
            b = Battle(cuserdex, oppuserdex, un, oppname)
            b.run()
            
            print(oppname, opp_user)
            summ = b.summary
            print(summ)
            if summ['winner'] == un:
                current_user.winner()
                opp_user.loser()
            elif summ['winner'] == oppname:
                current_user.loser()
                opp_user.winner()
            flash(f"{summ['winner']} WON THE BATTLE!!!", category='success')
            flash(f"It's a sad day for {summ['loser']}, they lost. . .", category='warning')
            return render_template('battle.html', b=b, summ=summ, ulist=ulist, cuserdex=cuserdex, oppuserdex=oppuserdex, oppname=oppname, opp_user=opp_user, bform=bform)
            

            
    return render_template('battle.html', ulist=ulist, cuserdex=cuserdex, oppuserdex=oppuserdex, oppname=oppname, bform=bform)