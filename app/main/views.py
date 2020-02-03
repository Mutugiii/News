from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,search_articles
from ..models import Article

@main.route('/')
def index():
    '''
    View root function to return index page and its data
    '''

    # Getting topics
    technology_articles = get_articles('technology')
    title = 'News Highlights'

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', search_word = search_article))
    return render_template('index.html', title = title, technology = technology_articles)

@main.route('/search/<search_word>')
def search(search_word):
    '''
    Function to search for content
    '''    
    searched_articles = search_articles(search_word)
    message = f'Search results for {search_word}'
    return render_template('search.html', message = message, search = searched_articles)