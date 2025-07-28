from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

print("Hello")

# SQL lite DB Connection.

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

# In-memory DB/Object
# books_list=[
#      {
#          'id': 0,
#          "author":"chinua achebe",
#          "language":"english",
#          "title":"things fall apart",
#      },
#      {
#          'id': 1,
#          "author": "hans christian andersen",
#          "language": "danish",
#          "title": "fairy tales",
#      },
#      {
#          'id': 2,
#          "author": "samuel beckett",
#          "language": "french,english",
#          "title": "molloy,malone dies,the unnamable,the triology",
#      },
#      {
#          'id': 6,
#          "author": "jorge luis borges",
#          "language": "spanish",
#          "title": "ficciones",
#      },
#      {
#          'id': 3,
#          "author": "giovanni boccaccio",
#          "language": "italian",
#          "title": "the decameron",
#      },
#      {
#          'id': 5,
#          "author": "emily bront",
#          "language": "english",
#          "title": "wuthering heights",
#      },
#  ]

# CRUD Operations

@app.route('/books', methods = ['GET', 'POST'])
def books():

    conn = db_connection()

    cursor = conn.cursor()

    if request.method == 'GET':
        sql = """ select * from book """
        cursor = cursor.execute(sql)

        #Converting the cursor object to a Dictionary.
        # fetchall will return list of tuples where each tuple will represent a row in DB
        books_list = [ { 'id' : row[0], 'author' : row[1], 'language' : row[2], 'title' : row[3] } for row in cursor.fetchall() ]

        if len(books_list) > 0:
            return jsonify(books_list), 200
        
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']

        sql = """ Insert into book (author, language, title) 
                  values(?, ?, ?)"""
        
        cursor = cursor.execute(sql, (new_author, new_language, new_title, ))

        conn.commit() # Helps you to commit the changes to the DB.

        return f"The Book has been added to the DB under the ID {cursor.lastrowid} ", 201
    

    return "Sorry We did not find the DB", 404


@app.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):

    conn = db_connection()

    cursor = conn.cursor()

    if request.method == 'GET':

        sql = """ select * from book where id = ? """

        cursor = cursor.execute(sql, (id,))

        requested_book = [ dict(id = row[0], author = row[1], language = row[2], title = row[3]) for row in cursor.fetchall() ]

        if len(requested_book) == 1:
            return jsonify(requested_book), 200
        else:
            return f"The requested book ID {id} is not present in the book DB"
    
    if request.method == 'PUT':
        
        title = request.form['title']
        language = request.form['language']
        author = request.form['author']

        sql = """ update book 
                  set title = ?,
                      language = ?,
                      author = ?
                  where id = ?
              """
        
        cursor = cursor.execute(sql, (title, language, author, id))

        cursor1 = cursor.execute("select * from book")

        book_list = [ dict(id = row[0], author = row[1], language = row[2], title = row[3]) for row in cursor1.fetchall() ]

        conn.commit()

        return jsonify(book_list), 200
    


    if request.method == 'DELETE':
        
        sql = """ delete from book where id = ? """

        cursor.execute(sql, (id,))

        conn.commit()

        cursor1 = cursor.execute("select * from book")

        deleted_book = [ dict(id = row[0], author = row[1], language = row[2], title = row[3]) for row in cursor1.fetchall() ]

        return jsonify(deleted_book), 200
    
    return "Sorry We did not find the DB", 404

            
        

if __name__ == '__main__':
    app.run(port=8000, debug=True)