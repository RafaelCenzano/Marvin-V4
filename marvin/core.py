from marvin import app, forms
from marvin.helpers import physics_helpers
from flask import render_template, redirect, url_for, request, flash

'''
Views
'''
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/home/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculators', methods=['GET'])
@app.route('/calculators/', methods=['GET'])
def calculators():
    return render_template('calculators.html')

@app.route('/calculators/kinematics', methods=['GET', 'POST'])
@app.route('/calculators/kinematics/', methods=['GET', 'POST'])
def kinematics():
    form = forms.KinematicsForm()
    if request.method == 'POST':
        count = 0
        if form.vi.data is not None:
            count += 1
        if form.vf.data is not None:
            count += 1
        if form.t.data is not None:
            count += 1
        if form.a.data is not None:
            count += 1
        if form.d.data is not None:
            count += 1
        if count >= 3:
            physicsdata = physics_helpers.kinematics.Kinematics(
                form.vi.data, form.vf.data, form.t.data, form.a.data, form.d.data)
            physicsdata.calculations()
            flash('Successfully calculated', 'success')
            return render_template(
                'kinematicsSuccess.html',
                physicsdata=physicsdata)
        flash('You need to input at least 3 givens', 'error')
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
