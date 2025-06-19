#!/usr/bin/python3

"""3. Python is cool!"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hb():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def ct(text):
    return f"C {text.replace('_', ' ')}"

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pt(text="is cool"):
    return f"Python {text.replace('_', ' ')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
