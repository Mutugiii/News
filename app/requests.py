import urllib.request,json
from .models import Source,Article

# Getting api key and base urls
api_key = None
article_base_url = None
source_base_url = None
search_base_url = None

def configure_request(app):
    global api_key,article_base_url,source_base_url,search_base_url
    api_key = app.config['NEWS_API_KEY']
    article_base_url = app.config['ARTICLE_BASE_URL']
    source_base_url = app.config['SOURCE_BASE_URL']
    search_base_url = app.config['SEARCH_BASE_URL']

def process_articles(article_dictionary):
    '''
    Function to process the resulting dictionary that  json.load creates from an api call

    Args:
        article_dictionary: Resulting dictionary of json.loads function
    '''
    articles_list = []
    for article in article_dictionary:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        image_url = article.get('urlToImage')
        date_published = article.get('publishedAt')
        content = article.get('content')

        if image_url:
            article_object = Article(author,title,description,url,image_url,date_published,content)
            articles_list.append(article_object)

    return articles_list


def get_articles(query):
    '''
    Function to get articles based on the topic or keyword
    '''
    article_details = json.loads(urllib.request.urlopen(article_base_url.format(query,api_key)).read())

    article_object = None
    if article_details['articles']:
        article_object = process_articles(article_details['articles'])
    return article_object

def search_articles(query):
    '''
    Function to get articles based on the topic or keyword
    '''
    article_details = json.loads(urllib.request.urlopen(search_base_url.format(query,api_key)).read())

    article_object = None
    if article_details['articles']:
        article_object = process_articles(article_details['articles'])
    return article_object

