from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_articles,search_articles,get_sources, get_source_articles
from ..models import Article

@main.route('/')
def index():
    '''
    View root function to return index page and its data
    '''

    # Getting topics
    technology_articles = get_articles('technology')
    title = 'News Highlights'

    source_pieces = get_sources()

    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('.search', search_word = search_article))
    return render_template('index.html', title = title, technology = technology_articles, sources = source_pieces)

@main.route('/search/<search_word>')
def search(search_word):
    '''
    Function to search for content
    '''    
    search_list =  search_word.split(" ")
    search_format = "+".join(search_list)
    searched_articles = search_articles(search_format)
    message = f'Search results for {search_word}'
    return render_template('search.html', message = message, search = searched_articles)

@main.route('/sources')
def sources():
    '''
    Function to display the sources
    '''
    source_pieces = get_sources()
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('.search', search_word = search_article))
    return render_template('sources.html', sources = source_pieces)

@main.route('/sources/<source_id>')
def source(source_id):
    '''
    Function to display individual function
    '''
    article_source = get_source_articles(source_id)
    return render_template('articles.html', source = article_source)