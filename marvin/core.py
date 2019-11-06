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
            try:
                temp = float(form.vi.data)
                count += 1
            except BaseException:
                flash('Initial Velocity must be a number', 'warning')
        if form.vf.data is not None:
            try:
                temp = float(form.vf.data)
                count += 1
            except BaseException:
                flash('Final Velocity must be a number', 'warning')
        if form.t.data is not None:
            try:
                temp = float(form.t.data)
                count += 1
            except BaseException:
                flash('Time must be a number', 'warning')
        if form.a.data is not None:
            try:
                temp = float(form.a.data)
                count += 1
            except BaseException:
                flash('Acceleration must be a number', 'warning')
        if form.d.data is not None:
            try:
                temp = float(form.d.data)
                count += 1
            except BaseException:
                flash('Delta Distance must be a number', 'warning')
        if count >= 3:
            physicsdata = physics_helpers.kinematics.Kinematics(
                physics_helpers.numberProcessing.formCleanup(form.vi.data),
                physics_helpers.numberProcessing.formCleanup(form.vf.data),
                physics_helpers.numberProcessing.formCleanup(form.t.data),
                physics_helpers.numberProcessing.formCleanup(form.a.data),
                physics_helpers.numberProcessing.formCleanup(form.d.data))
            physicsdata.calculations()
            flash('Successfully calculated!', 'success')
            return render_template(
                'kinematicsSuccess.html',
                physicsdata=physicsdata)
        flash('You need to input at least 3 givens', 'error')
    return render_template('kinematics.html', form=form)


@app.route('/calculators/sigfigs', methods=['GET', 'POST'])
@app.route('/calculators/sigfigs/', methods=['GET', 'POST'])
def sigfigs():
    form = forms.SigFigForm()
    if request.method == 'POST':
        if form.validate():
            sigFigCount = physics_helpers.numberProcessing.count_sig_figs(
                form.num.data)
            flash('Successfully counted!', 'success')
            return render_template(
                'sigfigsSuccess.html',
                sigFigCount=sigFigCount)
        flash('You need to input a value', 'error')
    return render_template('sigfigs.html', form=form)


'''
Error Handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
'''
