class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        id = self.id
        name = self.name
        description = self.description
        url = self.url
        category = self.category
        language = self.language
        country = self.country 

class Article:
    '''
    Article class to define article objectsa

    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        author = self.author
        title = self.title
        description = self.description
        url = self.url
        urlToImage = self.urlToImage
        publishedAt = self.publishedAt
        content = self.content
