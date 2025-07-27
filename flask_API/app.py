from flask import Flask, jsonify, request

app = Flask(__name__)

print("Hello")

# In-memory DB/Object
books_list=[
     {
         'id': 0,
         "author":"chinua achebe",
         "language":"english",
         "title":"things fall apart",
     },
     {
         'id': 1,
         "author": "hans christian andersen",
         "language": "danish",
         "title": "fairy tales",
     },
     {
         'id': 2,
         "author": "samuel beckett",
         "language": "french,english",
         "title": "molloy,malone dies,the unnamable,the triology",
     },
     {
         'id': 6,
         "author": "jorge luis borges",
         "language": "spanish",
         "title": "ficciones",
     },
     {
         'id': 3,
         "author": "giovanni boccaccio",
         "language": "italian",
         "title": "the decameron",
     },
     {
         'id': 5,
         "author": "emily bront",
         "language": "english",
         "title": "wuthering heights",
     },
 ]

# CRUD Operations

@app.route('/books', methods = ['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list), 200
        else:
            return 'Nothing found', 404
    
    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']

        new_id = books_list[-1]['id'] + 1

        new_books_list = {
            'id' : new_id,
            'author' : new_author,
            'language' : new_language,
            'title' : new_title 
        }

        books_list.append(new_books_list)

        return jsonify(books_list), 201
    
    else:
        return 'Nothing Found', 404
    
@app.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book), 200
        
        return 'No such Book ID present', 404
    
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['title'] = request.form['title']
                book['language'] = request.form['language']
                book['author'] = request.form['author']

                updated_book = {
                    'id' : book['id'],
                    'title' : book.title,
                    'language' : book.language,
                    'author' : book.author
                }

                return jsonify(updated_book), 201
            
        else:
            new_book = {
                'id' : id,
                'title' : request.form['title'],
                'language' : request.form['language'],
                'author' : request.form['author']
            }

            books_list.append(new_book)

            return jsonify(books_list), 200

    
    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)

                return jsonify(books_list), 200

            
        

if __name__ == '__main__':
    app.run(port=8000, debug=True)