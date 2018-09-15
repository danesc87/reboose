#!/usr/bin/python3
# Views for serie settings model includes SerieType and SerieGenre
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc
from app.models import SerieType
from app.utilities import is_not_json_request, check_empty_values
from app.custom_messages import succesfully_stored_on_db, succesfully_deleted_from_db

from app import app, db
from . import serie_path, serie_type_path, serie_genre_path


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

    return succesfully_stored_on_db(
        serie_type + 'type'
    ), 201