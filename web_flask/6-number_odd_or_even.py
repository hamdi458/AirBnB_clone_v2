#!/usr/bin/python3
"""Flask"""

from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """num_temp"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        paire_im = 'even'
    else:
        paire_im = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           paire_im=paire_im)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
