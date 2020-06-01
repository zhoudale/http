from flask import Flask, request, abort
import click

app = Flask(__name__)

@app.route('/')
@app.route('/hello', methods = ['GET', 'POST'])
def index():
    return '<h1>Hello</h1>',302,{'Location':'https://www.baidu.com'}
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


@app.route('/brew')
def tea():
    abort(418)

@app.cli.command()
def greet():
    """Say Hi"""
    click.echo('Hello!')


@app.route('/user', methods=['POST'])
def user():
    name = request.args.get('name', 'Human')
    return f'<h1>Hi, {name}</h1>'


@app.route('/go_back/<int:year>')
def to_year(year):
    return f'<h1>Welcome to year {2020-year}</h1>'
