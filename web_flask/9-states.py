#!/usr/bin/python3
"""
    A script that starts a flask web application
    and routes it to different urls on host 0.0.0.0
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state():
    """Return the page for this path"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Return the page for this path"""
    for state in storage.all(State).values():
        if id == state.id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """Return the page for this path"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
