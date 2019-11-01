from marvin import app, helpers, forms
from flask import render_template, redirect, url_for

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
    form = forms.KinematicsForm(csrf_enabled=False)
    if form.validate_on_submit():
        return redirect('/success')
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