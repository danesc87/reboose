#!/usr/bin/python3
# Views for author model
'''
 Author: Daniel Córdova A.
'''

from flask import abort, request
from flask import jsonify

from app import app, db, custom_messages
from app.models import Author
from . import author_path


@app.route(author_path, methods=['POST'])
def post_author():
    if not request.json:
        abort(400)

    author_name = request.json.get('name')
    author_lastname = request.json.get('lastname')
    existing_author = Author.query.filter_by(name=author_name, lastname=author_lastname).first()
    if existing_author != None:
        abort(400)
    new_author = Author(name=author_name, lastname=author_lastname)
    db.session.add(new_author)
    db.session.commit()
    return custom_messages.succesfully_stored_on_db("Author " + author_name + " " + author_lastname), 201

@app.route(author_path, methods=['GET'])
def get_authors():
    all_authors = Author.query.all()

    return jsonify([author.json_dump() for author in all_authors])

@app.route(author_path, methods=['DELETE'])
def delete_author():
    if not request.json:
        abort(400)

    author_name = request.json.get('name')
    author_lastname = request.json.get('lastname')
    deleted_author = Author.query.filter_by(name=author_name, lastname=author_lastname).\
        order_by(Author.id.desc()).first()
    if deleted_author == None:
        abort(404)
    db.session.delete(deleted_author)
    db.session.commit()
    return custom_messages.succesfully_deleted_from_db("Author " + author_name + " " + author_lastname)