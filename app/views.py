from flask import render_template, request
from app import app, db
from .models import BookType

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Reboose Home Page')

@app.route('/settings')
def settings():
    return render_template('settings.html', title='Reboose Settings')

@app.route('/booksettings', methods=['GET', 'POST'])
def post_booksettings():
    if request.method == 'GET':
        return render_template('booksettings.html', title='Reboose Book Settings', types = BookType.query.all())
    if request.method == 'POST':
        type_of_book = request.form['type']
        if type_of_book != '' or type_of_book != None:
            new_book_type = BookType(type=type_of_book)
            db.session.add(new_book_type)
            db.session.commit()
        return render_template('booksettings.html', title='Reboose Book Settings')

@app.route('/seriessettings', methods=['GET', 'POST'])
def seriessettings():
    return render_template('seriessettings.html', title='Reboose Series Settings')
