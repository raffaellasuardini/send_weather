from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired, Email


##WTForm

class RegistrationForm(FlaskForm):
    email = StringField('Inserisci la tua email', validators=[DataRequired('Inserisci una email'), Email('Email non valida')])
    location = StringField('Inserisci la città', validators=[DataRequired('Inserisci una location')])
    time = TimeField('Mandami il meteo ogni giorno alle: ', format='%H:%M', validators=[DataRequired('Inserisci un orario')])
    submit = SubmitField('Invia')
