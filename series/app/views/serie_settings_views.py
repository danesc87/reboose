#!/usr/bin/python3
# Views for serie settings model includes SerieType and SerieGenre
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify
from sqlalchemy import exc

from app import app, db
from . import serie_path, serie_type_path, serie_genre_path


#############
# Book Types#
#############

@app.route(serie_path + serie_type_path, methods=['POST'])
def post_new_serie_type():
    print('Hola')
    return jsonify({'message': 'It Worked!'})