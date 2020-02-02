import unittest
from app.models import models

class TestArticle(unittest.TestCase):
    '''
    Test class for articles class

    Args:
        unittest.TestCase: 
    '''
    def setUp(self):
        '''
        To set up before every test
        '''
        self.new_article = Article('Kamau Ngwiri', 'BBI in Kenya', 'BBI is wasting time!', 'nation.co.ke', 'img.nation.co.ke','2019-04-12T10:55:00Z','This is too long')

    def test_instance(self):
        '''
        Test that the initialized article is an instance of the model class
        '''
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test that it is initialized properly
        '''
        self.assertEqual(self.new_article.author,'Kamau Ngwiri')
        self.assertEqual(self.new_article.title, 'BBI in Kenya')
        self.assertEqual(self.new_article.description, 'BBI is wasting time!')
        self.assertEqual(self.new_article.url, 'nation.co.ke')
        self.assertEqual(self.new_article.urlToImage,'img.nation.co.ke')
        self.assertEqual(self.new_article.publishedAt,'2019-04-12T10:55:00Z')
        self.assertEqual(self.new_article.content, 'This is too long')
