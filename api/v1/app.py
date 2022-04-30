#!/usr/bin/python3
"""Portal application"""
from models import storage
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
# from dotenv import load_dotenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """Colse connection"""
    storage.close()

@app.errorhandler(404)
def error_notfound(error):
    """featuring 404 error page"""
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
#    load_dotenv()
    app.run(host=host, port=port, threaded=True, debug=True)
