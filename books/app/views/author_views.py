#!/usr/bin/python3
# Views for author model
'''
 Author: Daniel Córdova A.
'''

from flask import jsonify
from flask import request

from app import app, db, custom_messages
from app.models import Author
from app.utilities import exist_object_on_database, duplicate_object_in_database
from app.utilities import is_not_json_request, check_empty_values
from . import book_path, author_path


@app.route(book_path + author_path, methods=['POST'])
def post_author():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    author_name = request.json.get('name')
    author_lastname = request.json.get('lastname')
    existing_author = Author.query.filter_by(name=author_name, lastname=author_lastname).first()
    duplicate_object_in_database(existing_author)
    new_author = Author(name=author_name, lastname=author_lastname)
    db.session.add(new_author)
    db.session.commit()
    return custom_messages.succesfully_stored_on_db(
        "Author " + author_name + " " + author_lastname
    ), 201


@app.route(book_path + author_path, methods=['GET'])
def get_authors():

    all_authors = Author.query.all()
    return jsonify(
        [author.json_dump() for author in all_authors]
    )


@app.route(book_path + author_path, methods=['DELETE'])
def delete_author():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    author_name = request.json.get('name')
    author_lastname = request.json.get('lastname')
    deleted_author = Author.query.filter_by(
        name=author_name,
        lastname=author_lastname
    ).order_by(
        Author.id.desc()
    ).first()
    exist_object_on_database(deleted_author)
    db.session.delete(deleted_author)
    db.session.commit()
    return custom_messages.succesfully_deleted_from_db(
        "Author " + author_name + " " + author_lastname
    )