from flask import make_response
from flask import jsonify
from app import app

@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)
