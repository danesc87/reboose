from flask import render_template, request
from app import app, db
from .models import BookType
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Daniel'}
    posts = [{
        'author': {'nickname': 'John'},
        'body': 'Chilly in Quito'
    },
    {
        'author': {'nickname': 'Gaby'},
        'body': 'I like thriller movies'
    }]
    return render_template('index.html', title='Reboose Home Page', user=user, posts=posts)

@app.route('/settings')
def settings():
    return render_template('settings.html', title='Reboose Settings')

@app.route('/booksettings', methods=['GET'])
def get_booksettings():
    return render_template('booksettings.html', title='Reboose Book Settings')

@app.route('/booksettings', methods=['POST'])
def post_booksettings():
    json_books = json.loads(request.data)
    for type_of_book in json_books:
        try:
            book_type = json.loads(type_of_book)['type']
        except TypeError:
            book_type = type_of_book['type']
        new_book_type = BookType(type=book_type)
        db.session.add(new_book_type)
        db.session.commit()

@app.route('/seriessettings', methods=['GET', 'POST'])
def seriessettings():
    return render_template('seriessettings.html', title='Reboose Series Settings')
