from marvin import app, helpers
from flask import render_template, redirect, url_for

'''
Views
'''
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


'''
Error Handlers
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
