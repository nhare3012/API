from flask_restful import Resource
from repository import Repository
from flask import request

repo=Repository()



class BookList(Resource):
    def __init__(self, repo=Repository):
        self.repo = repo

    def get(self):
        return [book.__dict__ for book
                 in self.repo.books_get_all()]

    def post(self, req=request):
        data = request.get_json()
        return self.repo.book_add(data).__dict__

class Book(Resource):
    def get(self, book_id):
        return {'hello': f'from book {book_id}'}


class ReviewList(Resource):
    def get(self, book_id):
       return [review.__dict__ for review
               in repo.reviews_get_by_book_id(int(book_id))]

class Review(Resource):
    def post(self):
        data = request.get_json()
        return repo.review_add(data).__dict__

        