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
        series_type = request.json.get('type')
        check_empty_values(series_type)

        new_series_type = SeriesType(type=series_type)
        db.session.add(new_series_type)
        db.session.commit()
    except exc.IntegrityError:
        abort(400)

    return custom_messages.successfully_stored_on_db(
        series_type + ' type'
    ), 201


@app.route(series_path + series_type_path, methods=['GET'])
def get_all_types():
    all_series_types = SeriesType.query.all()
    return jsonify([serie_type.json_dump() for serie_type in all_series_types])


@app.route(series_path + series_type_path + '/<string:series_type_name>', methods=['GET'])
def get_type_by_name(series_type_name):

    check_empty_values(series_type_name)
    series_type = SeriesType.query.filter_by(
        type=series_type_name
    ).first()
    exist_data_on_database(series_type)
    return jsonify(
        series_type.json_dump()
    )


@app.route(series_path + series_type_path, methods=['DELETE'])
def delete_type_by_name():

    is_not_json_request(request)
    series_type = request.json.get('type')
    check_empty_values(series_type)
    deleted_series_type = SeriesType.query.filter_by(
        type=series_type
    ).order_by(
        SeriesType.id.desc()
    ).first()
    exist_data_on_database(deleted_series_type)
    db.session.delete(deleted_series_type)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        series_type + " type"
    )

#################
# Series Genres #
################


@app.route(series_path + series_genre_path, methods=['POST'])
def post_new_genre():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    series_type = request.json.get('type')
    series_genre = request.json.get('genre')
    existing_series_genre = SeriesGenre.query.filter_by(
        genre=series_genre,
        type=series_type
    ).first()
    duplicate_data_in_database(existing_series_genre)
    new_series_genre = SeriesGenre(genre=series_genre, type=series_type)
    db.session.add(new_series_genre)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        series_genre + " " + series_type + " genre"
    ), 201


@app.route(series_path + series_genre_path, methods=['GET'])
def get_all_genres():

    all_series_genres = SeriesGenre.query.all()
    return jsonify(
        [series_genre.json_dump() for series_genre in all_series_genres]
    )


@app.route(series_path + series_genre_path + '/<string:series_type_name>', methods=['GET'])
def get_genre_by_type_and_name(series_type_name):

    check_empty_values(series_type_name)
    all_series_genres_by_type = SeriesGenre.query.filter_by(
        type=series_type_name
    ).all()
    exist_data_on_database(all_series_genres_by_type)
    return jsonify(
        [series_genre.json_dump() for series_genre in all_series_genres_by_type]
    )


@app.route(series_path + series_genre_path + '/<string:series_type_name>/<string:series_genre_name>', methods=['GET'])
def get_series_genre_by_type_and_genre(series_type_name, series_genre_name):

    check_empty_values(series_type_name)
    check_empty_values(series_genre_name)
    series_genre = SeriesGenre.query.filter_by(
        genre=series_genre_name,
        type=series_type_name
    ).first()
    exist_data_on_database(series_genre)
    return jsonify(
        series_genre.json_dump()
    )


@app.route(series_path + series_genre_path, methods=['DELETE'])
def delete_genre_by_name():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    deleted_series_genre = SeriesGenre.query.filter_by(
        genre=request.json.get('genre'),
        type=request.json.get('type')
    ).order_by(
        SeriesGenre.id.desc()
    ).first()
    exist_data_on_database(deleted_series_genre)
    db.session.delete(deleted_series_genre)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        request.json.get('genre') + " " + request.json.get('type') + " genre"
    )
