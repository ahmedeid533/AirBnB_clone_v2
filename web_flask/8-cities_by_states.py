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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays 'n is a number' """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
