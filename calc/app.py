# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_params():
    #TODO: make function to add query string parameters a and b.

@app.route('/sub')
def sub_params():
    #TODO: make function to subtract query string parameter b from query string parameter a.

@app.route('/mult')
def mult_params():
    #TODO: make function to multiply query string parameters a and b.

@app.route('/div')
def div_params():
    #TODO: make function to divide query string parameter a by query string parameter b.