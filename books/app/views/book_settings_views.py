#!/usr/bin/python3
# Views for book settings model includes BookType and BookGenre
"""
 Author: Daniel Córdova A.
"""

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc

from app import app, db, custom_messages
from app.models import BookType, BookGenre
from app.utilities import exist_data_on_database, duplicate_data_in_database
from app.utilities import is_not_json_request, check_empty_values
from . import book_path, book_type_path, book_genre_path


##############
# Book Types #
##############


@app.route(book_path + book_type_path, methods=['POST'])
def post_type():

    is_not_json_request(request)
    try:
        type_name = request.json.get('type_name')
        check_empty_values(type_name)

        new_type_name = BookType(type_name=type_name)
        db.session.add(new_type_name)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.successfully_stored_on_db(
        type_name + " type"
    ), 201


@app.route(book_path + book_type_path, methods=['GET'])
def get_all_types():
    all_types_names = BookType.query.all()
    return jsonify([type_name.json_dump() for type_name in all_types_names])


@app.route(book_path + book_type_path + '/<string:type_name>', methods=['GET'])
def get_type_by_name(type_name):
    check_empty_values(type_name)
    book_type_name = BookType.query.filter_by(
        type_name=type_name
    ).first()
    exist_data_on_database(book_type_name)
    return jsonify(
        book_type_name.json_dump()
    )


@app.route(book_path + book_type_path, methods=['DELETE'])
def delete_type_by_name():

    is_not_json_request(request)
    type_name = request.json.get('type_name')
    check_empty_values(type_name)
    deleted_type_name = BookType.query.filter_by(
        type_name=type_name
    ).order_by(
        BookType.id.desc()
    ).first()
    exist_data_on_database(deleted_type_name)
    db.session.delete(deleted_type_name)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        type_name + " type_name"
    )

##############
# Book Genre #
##############


@app.route(book_path + book_genre_path, methods=['POST'])
def post_genre():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    type_name = request.json.get('type_name')
    book_genre = request.json.get('genre')
    existing_book_genre = BookGenre.query.filter_by(
        genre=book_genre,
        type_name=type_name
    ).first()
    duplicate_data_in_database(existing_book_genre)
    new_genre_name = BookGenre(genre=book_genre, type_name=type_name)
    db.session.add(new_genre_name)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        book_genre + " " + type_name + " genre"
    ), 201


@app.route(book_path + book_genre_path, methods=['GET'])
def get_all_genres():

    all_genre_names = BookGenre.query.all()
    return jsonify(
        [genre_name.json_dump() for genre_name in all_genre_names]
    )


@app.route(book_path + book_genre_path + '/<string:type_name>', methods=['GET'])
def get_genre_by_type(type_name):

    check_empty_values(type_name)
    all_genre_names_by_type = BookGenre.query.filter_by(
        type_name=type_name
    ).all()
    exist_data_on_database(all_genre_names_by_type)
    return jsonify(
        [genre_name.json_dump() for genre_name in all_genre_names_by_type]
    )


@app.route(book_path + book_genre_path + '/<string:type_name>/<string:genre_name>', methods=['GET'])
def get_book_genre_by_type_and_genre(type_name, genre_name):

    check_empty_values(type_name)
    check_empty_values(genre_name)
    genre_name = BookGenre.query.filter_by(
        genre=genre_name,
        type_name=type_name
    ).first()
    exist_data_on_database(genre_name)
    return jsonify(
        genre_name.json_dump()
    )


@app.route(book_path + book_genre_path, methods=['DELETE'])
def delete_genre_by_name():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    deleted_genre_name = BookGenre.query.filter_by(
        genre=request.json.get('genre'),
        type_name=request.json.get('type_name')
    ).order_by(
        BookGenre.id.desc()
    ).first()
    exist_data_on_database(deleted_genre_name)
    db.session.delete(deleted_genre_name)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        request.json.get('genre') + " " + request.json.get('type_name') + " genre"
    )
