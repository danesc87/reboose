from flask import render_template, jsonify
from flask import abort, request
from app import app, db
from .models import BookType

@app.route('/booksettings', methods=['GET'])
def get_book_types():
    all_book_types = BookType.query.all()

    return jsonify([book_type.json_dump() for book_type in all_book_types])

@app.route('/booksettings/<int:book_type_id>', methods=['GET'])
def get_boot_type_by_id(book_type_id):
    book_type = BookType.query.get(book_type_id)
    if book_type == None:
        abort(404)

    return jsonify(book_type.json_dump())

@app.route('/booksettings/<string:book_type_name>', methods=['POST'])
def post_new_book_by_name(book_type_name):
    if book_type_name == '' or book_type_name == None:
        abort(404)

    new_book_type = BookType(type=book_type_name)
    db.session.add(new_book_type)
    db.session.commit()
    return jsonify({'message': 'Succesfully stored in DB!'})

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
