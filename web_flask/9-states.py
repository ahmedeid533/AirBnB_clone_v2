#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """ Displays 'n is a number' """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ Displays 'n is a number' """
    states = storage.all("State")
    if "State.{}".format(id) in states:
        states = states["State.{}".format(id)]
    else:
        states = None
    return render_template('9-states.html', state=states)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
