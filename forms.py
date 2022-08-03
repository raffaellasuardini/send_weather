from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email


##WTForm

class RegistrationForm(FlaskForm):
    email = StringField('Inserisci la tua email',
                        validators=[DataRequired('Inserisci una email'), Email('Email non valida')])
    location = StringField('Inserisci la città', validators=[DataRequired('Inserisci una location')])
    lat = HiddenField()
    lng = HiddenField()
    submit = SubmitField('Invia')


class UnsusbscribeForm(FlaskForm):
    email = StringField('Inserisci la email di registrazione',
                        validators=[DataRequired('Inserisci una email'), Email('Email non valida')])
    submit = SubmitField('Invia')


class ChangeCityForm(FlaskForm):
    email = StringField('Inserisci la email di registrazione',
                        validators=[DataRequired('Inserisci una email'), Email('Email non valida')])
    location = StringField('Inserisci una nuova città', validators=[DataRequired('Inserisci una location')])
    lat = HiddenField()
    lng = HiddenField()
    submit = SubmitField('Invia')
