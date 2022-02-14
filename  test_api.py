import routes
from models import BookModel 
from unittest.mock import patch 
from unittest import TestCase 
import unittest
from app import app
import json

BASE_URL = "/api/bookreactions"
book1 = BookModel('test 1', 'J R R Tolkien', 1)
book2 = BookModel('test 2', 'J R R Tolkien', 2)

class APITests(TestCase):

     @patch('routes.BookList.get')
     def test_books(self, test_patch):
         with app.test_client() as client:
            test_patch.return_value = [book1.__dict__, book2.__dict__]
            response = client.get(f'{BASE_URL}/Books')
            assert response.status_code == 200
            books = json.loads(response.data)
            assert books[0]['bookId'] == 1



    