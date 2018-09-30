#!/usr/bin/python3
# Views for series settings model includes SeriesType and SeriesGenre
"""
 Author: Daniel Córdova A.
"""

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc

from app import app, db
from app import custom_messages
from app.models import SeriesType, SeriesGenre
from app.utilities import exist_data_on_database, duplicate_data_in_database
from app.utilities import is_not_json_request, check_empty_values
from . import series_path, series_type_path, series_genre_path


################
# Series Types #
###############

@app.route(series_path + series_type_path, methods=['POST'])
def post_type():
    is_not_json_request(request)
    try:
        type_name = request.json.get('type_name')
        check_empty_values(type_name)

        new_type_name = SeriesType(type_name=type_name)
        db.session.add(new_type_name)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.successfully_stored_on_db(
        type_name + ' type'
    ), 201


@app.route(series_path + series_type_path, methods=['GET'])
def get_all_types():
    all_type_names = SeriesType.query.all()
    return jsonify([type_name.json_dump() for type_name in all_type_names])


@app.route(series_path + series_type_path + '/<string:type_name>', methods=['GET'])
def get_type_by_name(type_name):

    check_empty_values(type_name)
    series_type_name = SeriesType.query.filter_by(
        type_name=type_name
    ).first()
    exist_data_on_database(series_type_name)
    return jsonify(
        series_type_name.json_dump()
    )


@app.route(series_path + series_type_path, methods=['DELETE'])
def delete_type_by_name():

    is_not_json_request(request)
    type_name = request.json.get('type_name')
    check_empty_values(type_name)
    deleted_series_type = SeriesType.query.filter_by(
        type_name=type_name
    ).order_by(
        SeriesType.id.desc()
    ).first()
    exist_data_on_database(deleted_series_type)
    db.session.delete(deleted_series_type)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        type_name + " type"
    )

#################
# Series Genres #
################


@app.route(series_path + series_genre_path, methods=['POST'])
def post_new_genre():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    type_name = request.json.get('type_name')
    genre_name = request.json.get('genre')
    existing_series_genre = SeriesGenre.query.filter_by(
        genre=genre_name,
        type_name=type_name
    ).first()
    duplicate_data_in_database(existing_series_genre)
    new_series_genre = SeriesGenre(genre=genre_name, type_name=type_name)
    db.session.add(new_series_genre)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        genre_name + " " + type_name + " genre"
    ), 201


@app.route(series_path + series_genre_path, methods=['GET'])
def get_all_genres():

    all_genre_names = SeriesGenre.query.all()
    return jsonify(
        [genre_name.json_dump() for genre_name in all_genre_names]
    )


@app.route(series_path + series_genre_path + '/<string:type_name>', methods=['GET'])
def get_genre_by_type_and_name(type_name):

    check_empty_values(type_name)
    all_genre_names_by_type = SeriesGenre.query.filter_by(
        type_name=type_name
    ).all()
    exist_data_on_database(all_genre_names_by_type)
    return jsonify(
        [genre_name.json_dump() for genre_name in all_genre_names_by_type]
    )


@app.route(series_path + series_genre_path + '/<string:type_name>/<string:genre_name>', methods=['GET'])
def get_series_genre_by_type_and_genre(type_name, genre_name):

    check_empty_values(type_name)
    check_empty_values(genre_name)
    series_genre = SeriesGenre.query.filter_by(
        genre=genre_name,
        type_name=type_name
    ).first()
    exist_data_on_database(series_genre)
    return jsonify(
        series_genre.json_dump()
    )


@app.route(series_path + series_genre_path, methods=['DELETE'])
def delete_genre_by_name():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    deleted_series_name = SeriesGenre.query.filter_by(
        genre=request.json.get('genre'),
        type_name=request.json.get('type_name')
    ).order_by(
        SeriesGenre.id.desc()
    ).first()
    exist_data_on_database(deleted_series_name)
    db.session.delete(deleted_series_name)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        request.json.get('genre') + " " + request.json.get('type_name') + " genre"
    )