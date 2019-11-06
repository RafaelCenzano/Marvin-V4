from marvin import app, forms
from marvin.helpers import physics_helpers
from flask import render_template, redirect, url_for, request, flash, make_response

'''
Views
'''
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/home/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index/', methods=['GET'])
def index():
    page = make_response(render_template('index.html'))
    page.set_cookie('page', 'index', max_age=60 * 60 * 24 * 365)
    return page


@app.route('/calculators', methods=['GET'])
@app.route('/calculators/', methods=['GET'])
def calculators():
    page = make_response(render_template('calculators.html'))
    page.set_cookie('page', 'calculators', max_age=60 * 60 * 24 * 365)
    return page


@app.route('/calculators/kinematics', methods=['GET', 'POST'])
@app.route('/calculators/kinematics/', methods=['GET', 'POST'])
def kinematics():
    form = forms.KinematicsForm()
    if request.method == 'POST':
        count = 0
        if form.vi.data is not None:
            try:
                if form.vi.data is not None:
                    temp = float(form.vi.data)
                    count += 1
            except BaseException:
                flash('Initial Velocity must be a number', 'warning')
        if form.vf.data is not None:
            try:
                if form.vf.data is not None:
                    temp = float(form.vf.data)
                    count += 1
            except BaseException:
                flash('Final Velocity must be a number', 'warning')
        if form.t.data is not None:
            try:
                if form.t.data is not None:
                    temp = float(form.t.data)
                    count += 1
            except BaseException:
                flash('Time must be a number', 'warning')
        if form.a.data is not None:
            try:
                if form.a.data is not None:
                    temp = float(form.a.data)
                    count += 1
            except BaseException:
                flash('Acceleration must be a number', 'warning')
        if form.d.data is not None:
            try:
                if form.d.data is not None:
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
            page = make_response(
                render_template(
                    'kinematicsSuccess.html',
                    physicsdata=physicsdata))
            page.set_cookie(
                'page', 'kinematics', max_age=60 * 60 * 24 * 365)
            return page
        flash('You need to input at least 3 givens', 'error')
    page = make_response(render_template('kinematics.html', form=form))
    page.set_cookie('page', 'kinematics', max_age=60 * 60 * 24 * 365)
    return page


@app.route('/calculators/sigfigs', methods=['GET', 'POST'])
@app.route('/calculators/sigfigs/', methods=['GET', 'POST'])
def sigfigs():
    form = forms.SigFigForm()
    if request.method == 'POST':
        if form.num.data is not None:
            sigFigCount = physics_helpers.numberProcessing.count_sig_figs(
                physics_helpers.numberProcessing.formCleanup(form.num.data))
            flash('Successfully counted!', 'success')
            page = make_response(
                render_template(
                    'sigfigsSuccess.html',
                    sigFigCount=sigFigCount, num=form.num.data))
            page.set_cookie('page', 'sigfigs', max_age=60 * 60 * 24 * 365)
            return page
        flash('You need to input a value', 'error')
    page = make_response(render_template('sigfigs.html', form=form))
    page.set_cookie('page', 'sigfigs', max_age=60 * 60 * 24 * 365)
    return page


@app.route('/back')
@app.route('/back/')
def back():
    if 'page' in request.cookies:
        page = request.cookies['page']
        return redirect(url_for(page))
    else:
        return redirect(url_for('index'))


'''
Error Handlers

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
'''
