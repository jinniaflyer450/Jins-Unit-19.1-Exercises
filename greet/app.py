# https://stackoverflow.com/questions/29277581/flask-nameerror-name-app-is-not-defined Got some help with importing here.

from flask import Flask

app=Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns a message welcoming the user."""
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    """Returns a message welcoming the user home."""
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    """Returns a message welcoming the user back."""
    return 'welcome back'