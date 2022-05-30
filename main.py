from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)

class Table (db.Model):
    id = db.Column(db.Integer, primary_key=True)

#db.create_all()

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
