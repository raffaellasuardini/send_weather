from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
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



# db.create_all()

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


if __name__ == '__main__':
    app.run(debug=True)
