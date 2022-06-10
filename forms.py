from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, HiddenField
from wtforms.validators import DataRequired, Email


##WTForm

class RegistrationForm(FlaskForm):
    email = StringField('Inserisci la tua email', validators=[DataRequired('Inserisci una email'), Email('Email non valida')])
    location = StringField('Inserisci la città', validators=[DataRequired('Inserisci una location')])
    lat = HiddenField()
    lng = HiddenField()
    submit = SubmitField('Invia')
