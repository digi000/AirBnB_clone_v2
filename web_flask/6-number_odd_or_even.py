#!/usr/bin/python3

"""3. Python is cool!"""

from flask import Flask
from flask import render_template

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

@app.route('/number/<int:n>')
def nm(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def fn(n):
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def gh(n):
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
