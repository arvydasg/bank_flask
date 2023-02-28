from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
import app


def get_persons():
    return app.Person.query


def get_bank():
    return app.Bank.query


def get_pk(obj):
    return str(obj)


class PersonForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    surname = StringField("Surname", [DataRequired()])
    personal_id = StringField("Personal ID", [DataRequired()])
    phone_numer = StringField("Phone number", [DataRequired()])


class BankForm(FlaskForm):
    name = StringField("Name", [DataRequired()])
    address = StringField("Address", [DataRequired()])
    bank_code = StringField("Bank code", [DataRequired()])
    SWIFT_code = StringField("SWIFT code", [DataRequired()])


class Account(FlaskForm):
    number = StringField("Number", [DataRequired()])
    balance = IntegerField("Balance", [DataRequired()])
    person_id = QuerySelectField(
        query_factory=get_persons, allow_blank=True, get_label="name", get_pk=get_pk
    )
    bank_id = QuerySelectField(
        query_factory=get_bank, allow_blank=True, get_label="name", get_pk=get_pk
    )
