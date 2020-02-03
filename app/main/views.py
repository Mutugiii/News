from flask import render_template
from . import main
from ..requests import get_articles
from ..models import Article

@main.route('/')
def index():
    '''
    View root function to return index page and its data
    '''

    # Getting topics
    technology_articles = get_articles('Technology')
    title = 'News Highlights'
    return render_template('index.html', title = title, technology = technology_articles)

 