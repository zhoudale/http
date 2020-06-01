from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def index():
    return '<h1>Hello</h1>'
#
# @app.route('/greet/<name>')
# @app.route('/greet')
# def say_hello(name = 'Prog'):
#     return f'<h1>Hello, {name}!</h1>'
#

@app.route('/greet', defaults = {'name': 'Prog'})
@app.route('/greet/<name>')
def say_hello(name):
    return f'<h1>Hello, {name}!</h1>'
