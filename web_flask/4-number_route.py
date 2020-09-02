#!/usr/bin/python3
"""Flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display C <text> """
    return ("C %s" % text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """text"""
    return ("Python %s" % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ number"""
    return ("%d is a number" % n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
