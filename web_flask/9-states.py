#!/usr/bin/python3
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes: - /states_list """
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_cities(id):
    """ display HTML page with list of states """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down is executed """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
