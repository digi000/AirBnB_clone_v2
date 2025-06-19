#!/usr/bin/python3

"""0. Hello Flask!"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def f():
    """0. Hello Flask!"""
    return "Hello HBNB!"
