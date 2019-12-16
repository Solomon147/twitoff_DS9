"""Minimal flask app"""

from flask import Flask


#Make the applicatin
app = Flask(__name__)


#Make the route('@' is a decorator. its a function that takes in a function & return a function)
@app.route("/")


#Now define a function
def hello:
    return "Hello World!"