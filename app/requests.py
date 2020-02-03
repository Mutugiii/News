import urllib.request,json
from . import models

# Getting api key and base urls
api_key = None
article_base_url = None
source_base_url = None

def configure_request(app):
    global api_key,article_base_url,source_base_url
    api_key = app.config['NEWS_API_KEY']
    article_base_url = app.config['ARTICLE_BASE_URL']
    source_base_url = app.config['SOURCE_BASE_URL']


