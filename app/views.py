from flask import render_template, request, jsonify, abort
from app import app, db
from .models import BookType


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

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
