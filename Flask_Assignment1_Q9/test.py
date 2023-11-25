# Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for books (simulating a database)
books = [
    {"id": 1, "title": "Dopamine Detox", "author": "Thibaut Meurisse"},
    {"id": 2, "title": "Anxious People", "author": "Fredrik Backman"},
    {"id": 3, "title": "American Psycho", "author": "Bret Easton Ellis"},
    {"id": 4, "title": "White Noise", "author": "Don DeLillo"},
    # Add more books as needed
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

# PUT update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify(book), 200
    return jsonify({"message": "Book not found"}), 404

# DELETE a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
