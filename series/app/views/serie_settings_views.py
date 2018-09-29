#!/usr/bin/python3
# Views for serie settings model includes SerieType and SerieGenre
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc

from app import app, db
from app import custom_messages
from app.models import SerieType, SerieGenre
from app.utilities import exist_object_on_database, duplicate_object_in_database
from app.utilities import is_not_json_request, check_empty_values
from . import serie_path, serie_type_path, serie_genre_path


###############
# Serie Types #
###############

@app.route(serie_path + serie_type_path, methods=['POST'])
def post_new_serie_type():
    is_not_json_request(request)
    try:
        serie_type = request.json.get('type')
        check_empty_values(serie_type)

        new_serie_type = SerieType(type=serie_type)
        db.session.add(new_serie_type)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.succesfully_stored_on_db(
        serie_type + ' type'
    ), 201


@app.route(serie_path + serie_type_path, methods=['GET'])
def get_serie_type():
    all_serie_types = SerieType.query.all()
    return jsonify([serie_type.json_dump() for serie_type in all_serie_types])


@app.route(serie_path + serie_type_path + '/<string:serie_type_name>', methods=['GET'])
def get_serie_type_by_name(serie_type_name):

    check_empty_values(serie_type_name)
    serie_type = SerieType.query.filter_by(
        type=serie_type_name
    ).first()
    exist_object_on_database(serie_type)
    return jsonify(
        serie_type.json_dump()
    )


@app.route(serie_path + serie_type_path, methods=['DELETE'])
def delete_serie_type_by_name():

    is_not_json_request(request)
    serie_type = request.json.get('type')
    check_empty_values(serie_type)
    deleted_serie_type = SerieType.query.filter_by(
        type=serie_type
    ).order_by(
        SerieType.id.desc()
    ).first()
    exist_object_on_database(deleted_serie_type)
    db.session.delete(deleted_serie_type)
    db.session.commit()
    return custom_messages.succesfully_deleted_from_db(
        serie_type + " type"
    )

###############
# Serie Genre #
###############

@app.route(serie_path + serie_genre_path, methods=['POST'])
def post_new_genre():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    serie_type = request.json.get('type')
    serie_genre = request.json.get('genre')
    existing_serie_genre = SerieGenre.query.filter_by(
        genre=serie_genre,
        type=serie_type
    ).first()
    duplicate_object_in_database(existing_serie_genre)
    new_serie_genre = SerieGenre(genre=serie_genre, type=serie_type)
    db.session.add(new_serie_genre)
    db.session.commit()
    return custom_messages.succesfully_stored_on_db(
        serie_genre + " " + serie_type + " genre"
    ), 201

@app.route(serie_path + serie_genre_path, methods=['GET'])
def get_serie_genre():

    all_serie_genres = SerieGenre.query.all()
    return jsonify(
        [serie_genre.json_dump() for serie_genre in all_serie_genres]
    )

@app.route(serie_path + serie_genre_path + '/<string:serie_type_name>', methods=['GET'])
def get_serie_genre_by_type_name(serie_type_name):

    check_empty_values(serie_type_name)
    all_serie_genres_by_type = SerieGenre.query.filter_by(
        type=serie_type_name
    ).all()
    exist_object_on_database(all_serie_genres_by_type)
    return jsonify(
        [serie_genre.json_dump() for serie_genre in all_serie_genres_by_type]
    )


@app.route(serie_path + serie_genre_path + '/<string:serie_type_name>/<string:serie_genre_name>', methods=['GET'])
def get_serie_genre_by_type_and_genre(serie_type_name, serie_genre_name):

    check_empty_values(serie_type_name)
    check_empty_values(serie_genre_name)
    serie_genre = SerieGenre.query.filter_by(
        genre=serie_genre_name,
        type=serie_type_name
    ).first()
    exist_object_on_database(serie_genre)
    return jsonify(
        serie_genre.json_dump()
    )


@app.route(serie_path + serie_genre_path, methods=['DELETE'])
def delete_serie_genre_by_name():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    deleted_serie_genre = SerieGenre.query.filter_by(
        genre=request.json.get('genre'),
        type=request.json.get('type')
    ).order_by(
        SerieGenre.id.desc()
    ).first()
    exist_object_on_database(deleted_serie_genre)
    db.session.delete(deleted_serie_genre)
    db.session.commit()
    return custom_messages.succesfully_deleted_from_db(
        request.json.get('genre') + " " + request.json.get('type') + " genre"
    )
