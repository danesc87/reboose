#!/usr/bin/python3
# Views for books model
"""
 Author: Daniel Córdova A.
"""

from flask import jsonify
from flask import request

from app import app, db, custom_messages
from app.models import Book
from app.utilities import duplicate_data_in_database, list_must_have_items, exist_data_on_database
from app.utilities import is_not_json_request, check_empty_values
from . import book_path


@app.route(book_path, methods=['POST'])
def post_book():

    is_not_json_request(request)
    request_body = request.json
    book_name = request_body.get('book_name')
    book_type = request_body.get('book_type')
    book_genre = request_body.get('book_genre')
    book_author_name = request_body.get('book_author_name')
    book_author_last_name = request_body.get('book_author_last_name')

    [check_empty_values(request_body.get(field)) for field in request_body]

    existing_book = Book.query.filter_by(
        book_name=book_name,
        book_type=book_type,
        book_genre=book_genre,
        book_author_name=book_author_name,
        book_author_last_name=book_author_last_name
    ).first()

    duplicate_data_in_database(existing_book)

    new_book = Book(
        book_name=book_name,
        book_type=book_type,
        book_genre=book_genre,
        book_author_name=book_author_name,
        book_author_last_name=book_author_last_name
    )

    db.session.add(new_book)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        book_name + ' Book'
    ), 201


@app.route(book_path, methods=['GET'])
def get_all_books():

    all_books = Book.query.all()
    return jsonify(
        [each_book.json_dump() for each_book in all_books]
    )


@app.route(book_path + '/<string:book_name>', methods=['GET'])
def get_book_by_name(book_name):

    check_empty_values(book_name)
    books = Book.query.filter(Book.book_name.contains(book_name)).order_by(Book.id.desc())
    return jsonify(
        list_must_have_items([each_book.json_dump() for each_book in books])
    )


@app.route(book_path, methods=['DELETE'])
def delete_book():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    request_body = request.json
    deleted_book = Book.query.filter_by(
        book_name=request_body.get('book_name'),
        book_type=request_body.get('book_type'),
        book_genre=request_body.get('book_genre'),
        book_author_name=request_body.get('book_author_name'),
        book_author_last_name=request_body.get('book_author_last_name')
    ).order_by(
        Book.id.desc()
    ).first()
    exist_data_on_database(deleted_book)
    db.session.delete(deleted_book)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        "Book " + request_body.get('book_name')
    )
