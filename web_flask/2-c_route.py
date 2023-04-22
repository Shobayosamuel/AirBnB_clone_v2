#!/usr/bin/python3
"""
    A script that starts a flask web application
    and routes it to different urls
"""

from flask import Flask
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
    return f"C {ans}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
