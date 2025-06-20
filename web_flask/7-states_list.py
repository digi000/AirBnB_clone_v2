#!/usr/bin/python3

"""8. List of states"""
print("--- Script starting, importing modules... ---")
from models import storage
from flask import Flask
from models.state import State
from flask import render_template

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def statesd():
    nd = {}
    for state in storage.all(State).values():
        nd[state.id] = state.name
    return render_template('7-states_list.html', nd=nd)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
