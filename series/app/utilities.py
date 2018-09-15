#!/usr/bin/python3
# Some utilities for series
'''
 Author: Daniel Córdova A.
'''

from flask import abort

def is_not_json_request(request):
    if not request.json:
        abort(400)

def check_empty_values(value):
    if value == '' or value == None:
        abort(400)

def exist_object_on_database(object):
    if object == None:
        abort(404)

def duplicate_object_in_database(object):
    if object != None:
        abort(400)

def list_must_have_items(list):
    if len(list) < 1:
        abort(404)
    return list