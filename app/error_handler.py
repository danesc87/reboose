from flask import make_response
from flask import jsonify
from app import app

@app.errorhandler(400)
def bad_request_erro(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(500)
def internal_server_error(error):
    return make_response(jsonify({'error': 'There was an error on server side!'}), 500)