# https://github.com/DonatasNoreika/Python-pamokos/wiki/ORM-2-u%C5%BEduotis

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config["SECRET_KEY"] = "dfgsfdgsdfgsdfgsdf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "PersonBankAccount.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    personal_id = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=False)
    accounts = db.relationship("Account", backref="person")


class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    bank_code = db.Column(db.String(50), nullable=False)
    SWIFT_code = db.Column(db.String(50), nullable=False)
    accounts = db.relationship("Account", backref="bank")


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    bank_id = db.Column(db.Integer, db.ForeignKey("bank.id"))


if __name__ == "__main__":
    db.create_all()
    app.run(host="127.0.0.1", port=8000, debug=True)
