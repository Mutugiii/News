from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View root function to return index page and its data
    '''
    return render_template('index.html')

