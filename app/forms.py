from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FindPoke(FlaskForm):
    poke_name = StringField('Enter Pokemon name', validators=[DataRequired()])
    submit = SubmitField()