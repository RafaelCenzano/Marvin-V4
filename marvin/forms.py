from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

'''
Kinematics Form for Kinematics computation
'''


class KinematicsForm(FlaskForm):
    class Meta:
        csrf = False
    vi = StringField('Initial Velocity')
    vf = StringField('Final Velocity')
    a = StringField('Acceleration')
    t = StringField('Time')
    d = StringField('Delta Distance')
    submit = SubmitField('Calculate')


class SigFigForm(FlaskForm):
    class Meta:
        csrf = False
    num = StringField('Number to count')
    submit = SubmitField('Count')


class CalculatorForm(FlaskForm):
    class Meta:
        csrf = False
    display = StringField('Calculator input')
    submit = SubmitField('=')
    past = StringField('Calculator past')