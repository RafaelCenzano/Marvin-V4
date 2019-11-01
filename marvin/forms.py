from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField

'''
Kinematics Form for Kinematics computation
'''


class KinematicsForm(FlaskForm):
    class Meta:
        csrf = False
    vi = FloatField('Initial Velocity')
    vf = FloatField('Final Velocity')
    a = FloatField('Acceleration')
    t = FloatField('Time')
    d = FloatField('Delta Distance')
    submit = SubmitField('Calculate')
