#!/usr/bin/python2
# coding=utf-8
# @Date: 7/24/18
# @Author: HZH
"""

"""
from flask_wtf import Form
from wtforms import PasswordField, SubmitField, validators, StringField
from wtforms.fields.html5 import EmailField


class RegistrationForm(Form):
    email = EmailField("email", validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(),
        validators.Length(min=8, message="Please choose a password of at least 8 characters") ])
    password2 = PasswordField("password2", validators=[validators.DataRequired(),
        validators.EqualTo("password", message="Passwords must match")])
    submit = SubmitField("submit", validators=[validators.DataRequired()])


class LoginForm(Form):
    loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    loginpassword = PasswordField('password', validators=[validators.DataRequired(message="Password field is required")])
    submit = SubmitField('submit', validators=[validators.DataRequired()])

class CreateTableForm(Form):
    tablenumber = StringField('tablenumber', validators=[validators.DataRequired()])
    submit = SubmitField('createtablesubmit', validators=[validators.DataRequired()])