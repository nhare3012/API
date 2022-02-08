from flask import Flask
from flask_restful import Api
from routes import Book, BookList, Review, ReviewList
from flask_cors import CORS

BASE_URL = '/api/bookreactions'

app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(BookList, f'{BASE_URL}Books')
api.add_resource(Book, f'{BASE_URL}/Books/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews/<book_id>')
api.add_resource(Review, f'{BASE_URL}/Reviews')




if __name__ == '__main__':
    app.run(debug=True)
