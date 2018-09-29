#!/usr/bin/python3
# Custom messages for some actions
"""
 Author: Daniel Córdova A.
"""

from flask import jsonify


def successfully_stored_on_db(object_name):
    return jsonify({'message': '%s successfully stored in DB!' % object_name})


def successfully_deleted_from_db(object_name):
    return jsonify({'message': '%s successfully deleted from DB!' % object_name})
