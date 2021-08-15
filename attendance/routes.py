from flask import current_app as app
from flask import render_template, request, make_response
from . import db


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('main.html')
    if db.add_user(request.form['name'], request.form['password'], request.form['disco']):
        return render_template('main.html', extra='I got u bro')
    else:
        return render_template('main.html', extra='We already got u lol')


@app.errorhandler(404)
def error1(a):
    return make_response(render_template('error.html', page='Error 404', error='404'), 404)


@app.errorhandler(400)
def error2(a):
    return make_response(render_template('error.html', page='Error 400', error='400'), 400)


@app.errorhandler(500)
def error3(a):
    return make_response(render_template('error.html', page='Error 500', error='500'), 500)
