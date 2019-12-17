"""Minimal flask app"""

from flask import Flask, render_template


#Make the applicatin
app = Flask(__name__)


#Make the route('@' is a decorator. its a function that takes in a function & return a function)
@app.route("/")


#Now define a function
def hello():
    return render_template('home.html')



#Make a second route
@app.route("/about")

#Now make the function that goes with about
def preds():
    return render_template('about.html')