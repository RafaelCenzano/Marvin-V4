from marvin import app, forms
from marvin.helpers import physics
from flask import render_template, redirect, url_for, request, flash, make_response

'''
Views
'''
@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/home/', methods=['GET'])
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

        if form.vi.data != '':
            try:
                temp = float(form.vi.data)
                count += 1
            except BaseException:
                form.vi.data = ''
                flash(
                    'Initial Velocity must be a number, input number for initial velocity removed',
                    'warning')

        if form.vf.data != '':
            try:
                temp = float(form.vf.data)
                count += 1
            except BaseException:
                form.vf.data = ''
                flash(
                    'Final Velocity must be a number, input number for final velocity removed',
                    'warning')

        if form.t.data != '':
            try:
                temp = float(form.t.data)
                if abs(temp) != temp:
                    raise BaseException
                count += 1
            except BaseException:
                form.t.data = ''
                flash(
                    'Time must be a non negative number, input number for time removed',
                    'warning')

        if form.a.data != '':
            try:
                temp = float(form.a.data)
                count += 1
            except BaseException:
                form.a.data = ''
                flash(
                    'Acceleration must be a number, input number for acceleration removed',
                    'warning')

        if form.d.data != '':
            try:
                temp = float(form.d.data)
                if abs(temp) != temp:
                    raise BaseException
                count += 1
            except BaseException:
                form.d.data = ''
                flash(
                    'Delta Distance must be a non negative number, input number for delta distance removed',
                    'warning')

        if count >= 3:

            physicsdata = physics.kinematics.Kinematics(
                physics.numberProcessing.formCleanup(form.vi.data),
                physics.numberProcessing.formCleanup(form.vf.data),
                physics.numberProcessing.formCleanup(form.t.data),
                physics.numberProcessing.formCleanup(form.a.data),
                physics.numberProcessing.formCleanup(form.d.data))
            physicsdata.calculations()

            if physicsdata.initialVelocity is None or physicsdata.finalVelocity is None or physicsdata.time is None or physicsdata.acceleration is None or physicsdata.deltaDistance is None or abs(
                    physicsdata.deltaDistance) != physicsdata.deltaDistance or abs(physicsdata.time) != physicsdata.time:
                flash(
                    'Error with computing, couldn\'t compute or value was negative when it shounldn\'t have been negative',
                    'error')
                page = make_response(
                    render_template(
                        'kinematics.html',
                        form=form))
                page.set_cookie(
                    'page',
                    'kinematics',
                    max_age=60 * 60 * 24 * 365)
                return page

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

    num = form.num.data

    if request.method == 'POST':

        if form.num.data is None:
            flash('You need to input a number', 'error')

    check = False

    try:
        temp = float(num)
        check = True

    except BaseException:
        form.num.data = ''
        if request.method == 'POST':
            flash('Input must be a number, input number removed', 'warning')

    if check:
        num = physics.numberProcessing.count_sig_figs(
            physics.numberProcessing.formCleanup(form.num.data))

        flash('Successfully counted!', 'success')

    numCheck = False

    if num is not None and not isinstance(num, type('asds')):
        numCheck = True

    page = make_response(
        render_template(
            'sigfigs.html',
            form=form,
            number=form.num.data,
            num=num,
            numCheck=numCheck))
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
'''

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

'''
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
'''
