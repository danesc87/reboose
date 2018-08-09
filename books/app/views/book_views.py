#!/usr/bin/python3
# Views for books model
'''
 Author: Daniel Córdova A.
'''

from flask import jsonify
from flask import request

from app import app, db, custom_messages
from app.models import Book
from app.utilities import is_not_json_request, check_empty_values, duplicate_object_in_database, list_must_have_items
from . import book_path


@app.route(book_path, methods=['POST'])
def post_new_book():

    is_not_json_request(request)
    request_body = request.json
    book_name = request_body.get('book_name')
    book_type = request_body.get('book_type')
    book_genre = request_body.get('book_genre')
    book_author_name = request_body.get('book_author_name')
    book_author_lastname = request_body.get('book_author_lastname')

    [check_empty_values(request_body.get(field)) for field in request_body]

    existing_book = Book.query.filter_by(
        book_name=book_name,
        book_type=book_type,
        book_genre=book_genre,
        book_author_name=book_author_name,
        book_author_lastname=book_author_lastname
    ).first()

    duplicate_object_in_database(existing_book)

    new_book = Book(
        book_name=book_name,
        book_type=book_type,
        book_genre=book_genre,
        book_author_name=book_author_name,
        book_author_lastname=book_author_lastname
    )

    db.session.add(new_book)
    db.session.commit()
    return custom_messages.succesfully_stored_on_db\
               (book_name + ' Book'), 201


@app.route(book_path, methods=['GET'])
def get_all_books():

    all_books = Book.query.all()
    return jsonify([each_book.json_dump() for each_book in all_books])


@app.route(book_path + '/<string:book_name>', methods=['GET'])
def get_book_by_name(book_name):

    check_empty_values(book_name)
    books = Book.query.filter(Book.book_name.contains(book_name)).order_by(Book.id.desc())
    return jsonify(
        list_must_have_items([each_book.json_dump() for each_book in books])
    )
