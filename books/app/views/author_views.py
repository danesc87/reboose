#!/usr/bin/python3
# Views for author model
"""
 Author: Daniel Córdova A.
"""

from flask import jsonify
from flask import request

from app import app, db, custom_messages
from app.models import Author
from app.utilities import exist_data_on_database, duplicate_data_in_database
from app.utilities import is_not_json_request, check_empty_values
from . import book_path, author_path


@app.route(book_path + author_path, methods=['POST'])
def post_author():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    author_name = request.json.get('name')
    author_last_name = request.json.get('last_name')
    existing_author = Author.query.filter_by(name=author_name, last_name=author_last_name).first()
    duplicate_data_in_database(existing_author)
    new_author = Author(name=author_name, last_name=author_last_name)
    db.session.add(new_author)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        "Author " + author_name + " " + author_last_name
    ), 201


@app.route(book_path + author_path, methods=['GET'])
def get_all_authors():

    all_authors = Author.query.all()
    return jsonify(
        [author.json_dump() for author in all_authors]
    )


@app.route(book_path + author_path, methods=['DELETE'])
def delete_author():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    author_name = request.json.get('name')
    author_last_name = request.json.get('last_name')
    deleted_author = Author.query.filter_by(
        name=author_name,
        last_name=author_last_name
    ).order_by(
        Author.id.desc()
    ).first()
    exist_data_on_database(deleted_author)
    db.session.delete(deleted_author)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        "Author " + author_name + " " + author_last_name
    )
