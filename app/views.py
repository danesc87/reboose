from flask import render_template, jsonify
from flask import abort, request
from app import app, db, custom_messages
from .models import BookType

@app.route('/booktypes', methods=['GET'])
def get_book_types():
    all_book_types = BookType.query.all()

    return jsonify([book_type.json_dump() for book_type in all_book_types])

@app.route('/booktypes/<int:book_type_id>', methods=['GET'])
def get_boot_type_by_id(book_type_id):
    book_type = BookType.query.get(book_type_id)
    if book_type == None:
        abort(404)

    return jsonify(book_type.json_dump())

@app.route('/booktypes/<string:book_type_name>', methods=['POST'])
def post_new_book_by_name(book_type_name):
    if book_type_name == '' or book_type_name == None:
        abort(400)

    new_book_type = BookType(type=book_type_name)
    db.session.add(new_book_type)
    db.session.commit()
    return custom_messages.succesfully_stored_on_db(book_type_name)

@app.route('/booktypes/<string:book_type_name>', methods=['DELETE'])
def delete_book_type_by_name(book_type_name):
    if book_type_name == '' or book_type_name == None:
        abort(400)

    deleted_book_type = BookType.query.filter_by(type=book_type_name).order_by(BookType.id.desc()).first()
    if deleted_book_type == None:
        abort(404)
    db.session.delete(deleted_book_type)
    db.session.commit()
    return custom_messages.succesfully_deleted_from_db(book_type_name)



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Reboose Home Page')

@app.route('/settings')
def settings():
    return render_template('settings.html', title='Reboose Settings')

@app.route('/seriessettings', methods=['GET', 'POST'])
def seriessettings():
    return render_template('seriessettings.html', title='Reboose Series Settings')
