from models import BookModel, ReviewModel
from flask import current_app, g


class Repository():


    def get_db(self):
        if 'db'not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db

    def books_get_all(self):
        conn = self.get_db()
       
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("select title, author, bookId, cover from book order by title")
            book_records = ps_cursor.fetchall()
            book_list = []
            for row in book_records:
                book_list.append(BookModel(row[0], row[1], row[2], row[3]))
            ps_cursor.close()
        return book_list
        
        


    def book_get_by_id(self, book_id): 
        conn = self.get_db()
       
            
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("select title, author, bookId, cover from book where bookId = %s",[book_id])
            row = ps_cursor.fetchone()
            book = BookModel(row[0], row[1], row[2], row[3])
            ps_cursor.close()
        return book
        
    
    def book_add(self, data):
       conn = self.get_db()
        
            
       if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("INSERT INTO book(title, cover, author) VALUES (%s, %s, %s) RETURNING bookId ", (data['title'], data['cover'], data['author'] ) )
            conn.commit()
            id=ps_cursor.fetchone() [0]
            ps_cursor.close()
            book = BookModel(data['title'], data['author'], id, data['cover'])
       return book
        

    

    def reviews_get_by_book_id(self, book_id):
        conn = self.get_db()
       
            
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute("select content ,bookId, id from review where bookId = %s", [book_id])
            conn.commit()
            row = ps_cursor.fetchone()
            review =ReviewModel(row[0], row[1], row[2], row[3])
            ps_cursor.close()
        return review
       


      

    def review_add(self, data):
        conn = self.get_db()    
        if (conn):
            ps_cursor = conn.cursor()
            book_id = int(data['bookId'])
            ps_cursor.execute("INSERT INTO review (content,bookId) VALUES (%s, %s) RETURNING id ", (data['content']))
            conn.commit()
            id = ps_cursor.fetchone() [0]
            ps_cursor.close()
            review = ReviewModel(data['content'],book_id,id)
        return review
        


     

   

   


    