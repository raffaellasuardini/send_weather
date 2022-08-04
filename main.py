from flask import Flask
from flask import render_template, flash, redirect, url_for
import logging
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, UnsusbscribeForm, ChangeCityForm
from sender import Mail
from api import Weather
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', "sqlite:///db.db")
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    coord = db.Column(db.String(120), nullable=False)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    api_key = os.getenv('GOOGLE_KEY')
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        position = f'{form.lat.data} {form.lng.data}'
        already_user = User.query.filter_by(email=email).first()
        # email already in the database
        if position == ' ':
            flash("Attenzione: seleziona una città", 'alert-secondary')
            return redirect(url_for('hello_world'))
        if already_user:
            flash("Questa email riceve già il meteo", 'alert-secondary')
            return redirect(url_for('hello_world'))
        else:
            user = User(email=form.email.data, location=form.location.data, coord=position)
            db.session.add(user)
            db.session.commit()
            flash(f"Perfetto, ogni giorno riceverai il meteo di {form.location.data}", 'alert-success')
            return redirect(url_for('hello_world'))

    return render_template("index.html", form=form, key=api_key)


@app.route("/unsubscribe", methods=["GET", "POST"])
def unsubscribe():
    form = UnsusbscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            user_to_delete = User.query.get(user.id)
            db.session.delete(user_to_delete)
            db.session.commit()
            flash("Cancellazione avvenuta con successo. Ci mancherai 🌈", 'alert-success')
            return redirect('unsubscribe')
        else:
            flash(f"L'indirizzo {form.email.data} non è stato registrato", 'alert-danger')
            return render_template('unsubscribe.html', form=form)
    return render_template('unsubscribe.html', form=form)


@app.route("/change", methods=["GET", "POST"])
def change():
    api_key = os.getenv('GOOGLE_KEY')
    form = ChangeCityForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if user:
            user.location = form.location.data
            user.coord = f'{form.lat.data} {form.lng.data}'
            db.session.commit()
            flash(f"Riceverai il meteo per: {form.location.data}", 'alert-success')
            return render_template('change.html', form=form)
        else:
            flash(f"L'indirizzo {form.email.data} non è stato registrato", 'alert-danger')
            return render_template('change.html', form=form)
    return render_template('change.html', form=form, key=api_key)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
