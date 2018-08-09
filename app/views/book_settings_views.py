#!/usr/bin/python3
# Views for book settings model includes BookType and BookGenre
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc

from app import app, db, custom_messages
from app.models import BookType, BookGenre
from . import book_path, book_type_path, book_genre_path

@app.route(book_path + book_type_path, methods=['POST'])
def post_new_book_type():
    if not request.json:
        abort(400)
    try:
        book_type = request.json.get('type')
        new_book_type = BookType(type=book_type)
        db.session.add(new_book_type)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.succesfully_stored_on_db(book_type + " type"), 201

@app.route(book_path + book_type_path, methods=['GET'])
def get_book_types():
    all_book_types = BookType.query.all()
    return jsonify([book_type.json_dump() for book_type in all_book_types])

@app.route(book_path + book_type_path + '/<string:book_type_name>', methods=['GET'])
def get_boot_type_by_name(book_type_name):
    book_type = BookType.query.filter_by(type=book_type_name).first()
    if book_type == None:
        abort(404)

    return jsonify(book_type.json_dump())

@app.route(book_path + book_type_path + '/<string:book_type>', methods=['DELETE'])
def delete_book_type_by_name(book_type):
    if book_type == '' or book_type == None:
        abort(400)

    deleted_book_type = BookType.query.filter_by(type=book_type).order_by(BookType.id.desc()).first()
    if deleted_book_type == None:
        abort(404)
    db.session.delete(deleted_book_type)
    db.session.commit()

    return custom_messages.succesfully_deleted_from_db(book_type + " type")

@app.route(book_path + book_genre_path, methods=['POST'])
def post_new_genre():
    if not request.json:
        abort(400)

    try:
        request_body = request.json
        new_book_genre = BookGenre(genre=request_body.get('genre'), type=request_body.get('type'))
        db.session.add(new_book_genre)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.\
               succesfully_stored_on_db(request.json.get('genre') + " " + request.json.get('type') + " genre"), 201

@app.route(book_path + book_genre_path, methods=['GET'])
def get_book_genres():
    all_book_genres = BookGenre.query.all()
    return jsonify([book_genre.json_dump() for book_genre in all_book_genres])

@app.route(book_path + book_genre_path + '/<string:book_type_name>', methods=['GET'])
def get_book_genres_by_type_name(book_type_name):
    all_book_genres_by_type = BookGenre.query.filter_by(type=book_type_name).all()
    if all_book_genres_by_type == None:
        abort(404)

    return jsonify([book_genre.json_dump() for book_genre in all_book_genres_by_type])

@app.route(book_path + book_genre_path + '/<string:book_type_name>/<string:book_genre_name>', methods=['GET'])
def get_book_genre_by_type_and_genre(book_type_name, book_genre_name):
    if (book_type_name == '' or book_type_name == None) and (book_genre_name == '' or book_genre_name == None):
        abort(400)
    book_genre = BookGenre.query.filter_by(genre=book_genre_name, type=book_type_name).first()
    if book_genre == None:
        abort(404)
    return jsonify(book_genre.json_dump())

@app.route(book_path + book_genre_path, methods=['DELETE'])
def delete_book_genre_by_name():
    if not request.json:
        abort(400)

    deleted_book_genre = BookGenre.query.filter_by(genre=request.json.get('genre'), type=request.json.get(
        'type')).order_by(BookGenre.id.desc()).first()
    if deleted_book_genre == None:
        abort(404)
    db.session.delete(deleted_book_genre)
    db.session.commit()

    return custom_messages.\
        succesfully_deleted_from_db(request.json.get('genre') + " " + request.json.get('type') + " genre")

