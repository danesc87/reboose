#!/usr/bin/python3
# Views for books model
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify

from app import app, db, custom_messages
from . import book_path

from app.models import Book

@app.route(book_path, methods=['POST'])
def post_new_book():
    if not request.json:
        abort(400)

    request_body = request.json
    book_name = request_body.get('book_name')
    book_type = request_body.get('book_type')
    book_genre = request_body.get('book_genre')
    book_author_name = request_body.get('book_author_name')
    book_author_lastname = request_body.get('book_author_lastname')

    [check_empty_fields(request_body.get(field)) for field in request_body]

    new_book = Book(
        book_name=book_name,
        book_type=book_type,
        book_genre=book_genre,
        book_author_name=book_author_name,
        book_author_lastname=book_author_lastname
    )

    db.session.add(new_book)
    db.session.commit()

    return custom_messages.succesfully_stored_on_db(book_name + ' Book'), 201

@app.route(book_path, methods=['GET'])
def get_all_books():
    all_books = Book.query.all()
    return jsonify([each_book.json_dump() for each_book in all_books])

def check_empty_fields(field):
    if field == "" or field == None:
        abort(400)