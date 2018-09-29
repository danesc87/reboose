#!/usr/bin/python3
# Some utilities for books
"""
 Author: Daniel Córdova A.
"""

from flask import abort


def is_not_json_request(request):
    if not request.json:
        abort(400)


def check_empty_values(value):
    if value == '' or value is None:
        abort(400)


def exist_data_on_database(data):
    if data is None:
        abort(404)


def duplicate_data_in_database(data):
    if data is not None:
        abort(400)


def list_must_have_items(list_of_items):
    if len(list_of_items) < 1:
        abort(404)
    return list_of_items
