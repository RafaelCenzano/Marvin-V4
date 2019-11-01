from marvin import app, forms
from marvin.helpers import physics_helpers
from flask import render_template, redirect, url_for, request

'''
Views
'''
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/kinematics", methods=['GET', 'POST'])
def kinematics():
    form = forms.KinematicsForm()
    if request.method == 'POST':
        physicsdata = physics_helpers.kinematics.Kinematics(form.vi.data, form.vf.data, form.t.data, form.a.data, form.d.data)
        physicsdata.calculations()
        return render_template('kinematicsSuccess.html', physicsdata=physicsdata)
    return render_template('kinematics.html', form=form)


'''
Error Handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
'''