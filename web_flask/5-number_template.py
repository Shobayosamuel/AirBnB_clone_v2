#!/usr/bin/python3
"""
    A script that starts a flask web application
    and routes it to different urls
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """Return the page for this path"""
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """Return the page for this path"""
    return "HBNB"


@app.route('/c/<string:text>', methods=['GET'], strict_slashes=False)
def display_c(text):
    """Return the page for this path"""
    ans = text.replace('_', " ")
    return "C %s" % text


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<string:text>', methods=['GET'], strict_slashes=False)
def display_py(text="is cool"):
    """Return the page for this path"""
    ans = text.replace('_', " ")
    return "Python %s" % ans


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def display_num(n):
    """Return the page for this path"""
    return "%i is a number" % n


@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def num_template(n):
    """Return the page for this path"""
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
