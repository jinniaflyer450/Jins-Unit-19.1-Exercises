# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/<operation>')
def do_math(operation):
    args = request.args
    a = int(args['a'])
    b = int(args['b'])
    if(operation == 'add'):
        return str(add(a, b))
    elif(operation == 'sub'):
        return str(sub(a, b))
    elif(operation == 'mult'):
        return str(mult(a, b))
    elif(operation == 'div'):
        return str(div(a, b))

@app.route('/math/<operation>')
def do_math_alt_route(operation):
    args = request.args
    a = int(args['a'])
    b = int(args['b'])
    if(operation == 'add'):
        return str(add(a, b))
    elif(operation == 'sub'):
        return str(sub(a, b))
    elif(operation == 'mult'):
        return str(mult(a, b))
    elif(operation == 'div'):
        return str(div(a, b))     