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
from app.models import SerieType
from app.utilities import exist_object_on_database
from app.utilities import is_not_json_request, check_empty_values
from . import serie_path, serie_type_path


#############
# Book Types#
#############

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
        serie_type + 'type'
    ), 201


@app.route(serie_path + serie_type_path, methods=['GET'])
def get_series_types():
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
