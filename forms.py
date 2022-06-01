from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired, Email


##WTForm

class RegistrationForm(FlaskForm):
    email = StringField('Inserisci la tua email', validators=[DataRequired(), Email()])
    location = StringField('Inserisci la città')
    time = TimeField('Mandami il meteo ogni giorno alle: ', format='%H:%M')
    submit = SubmitField('Invia')
