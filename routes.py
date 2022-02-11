from flask_restful import Resource


class BookList(Resource):
    def get(self, ):
        return {'hello': 'from booklist'}

class Book(Resource):
    def get(self, book_id):
      return {'hello': f'from book {book_id}'}

class ReviewList(Resource):
    def get(self, book_id):
       return {'hello': f'from review book {book_id}'}

class Review(Resource):
    def get(self):
     return {'hello': 'from review'}