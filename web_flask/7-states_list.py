#!/usr/bin/python3
"""
    A script that starts a flask web application
    and routes it to different urls on host 0.0.0.0
"""
from flask import Flask
from flask import render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
