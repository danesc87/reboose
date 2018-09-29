#!/usr/bin/python3
# Views for series model
"""
 Author: Daniel Córdova A.
"""

from flask import jsonify
from flask import request

from app import app, db, custom_messages
from app.models import Series
from app.utilities import is_not_json_request, check_empty_values, duplicate_data_in_database, list_must_have_items, \
    exist_data_on_database
from . import series_path


@app.route(series_path, methods=['POST'])
def post_series():

    is_not_json_request(request)
    request_body = request.json
    series_name = request_body.get('series_name')
    series_type = request_body.get('series_type')
    series_genre = request_body.get('series_genre')

    [check_empty_values(request_body.get(field)) for field in request_body]

    existing_series = Series.query.filter_by(
        series_name=series_name,
        series_type=series_type,
        series_genre=series_genre
    ).first()

    duplicate_data_in_database(existing_series)

    new_series = Series(
        series_name=series_name,
        series_type=series_type,
        series_genre=series_genre
    )

    db.session.add(new_series)
    db.session.commit()
    return custom_messages.successfully_stored_on_db(
        series_name + ' Serie'
    ), 201


@app.route(series_path, methods=['GET'])
def get_all_series():

    all_series = Series.query.all()
    return jsonify(
        [each_series.json_dump() for each_series in all_series]
    )


@app.route(series_path + '/<string:series_name>', methods=['GET'])
def get_series_by_name(series_name):

    check_empty_values(series_name)
    series = Series.query.filter(Series.series_name.contains(series_name)).order_by(Series.id.desc())
    return jsonify(
        list_must_have_items([each_series.json_dump() for each_series in series])
    )


@app.route(series_path, methods=['DELETE'])
def delete_series():

    is_not_json_request(request)
    [check_empty_values(request.json.get(field) for field in request.json)]
    request_body = request.json
    deleted_series = Series.query.filter_by(
        series_name=request_body.get('series_name'),
        series_type=request_body.get('series_type'),
        series_genre=request_body.get('series_genre')
    ).order_by(
        Series.id.desc()
    ).first()
    exist_data_on_database(deleted_series)
    db.session.delete(deleted_series)
    db.session.commit()
    return custom_messages.successfully_deleted_from_db(
        "Series " + request_body.get('series_name')
    )
