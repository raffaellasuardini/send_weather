from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', "sqlite:///blog.db")
db = SQLAlchemy(app)


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)


# db.create_all()

@app.route("/", methods=["GET", "POST"])
def hello_world():
    registration_form = RegistrationForm()

    return render_template("index.html", form=registration_form)

if __name__ == '__main__':
    app.run(debug=True)
