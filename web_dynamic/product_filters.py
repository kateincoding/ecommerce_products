#!/usr/bin/python3
"""Starts a Flash Web Application"""


#!/usr/bin/python3
"""Portal application"""
from models import storage
from models.product import Product
from models.category import Category
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
# from dotenv import load_dotenv
# from api.v1.views import app_views

app = Flask(__name__)
# app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """Colse connection"""
    storage.close()

@app.errorhandler(404)
def error_notfound(error):
    """featuring 404 error page"""
    return make_response(jsonify({'error': "Not found"}), 404)


@app.route('/mvp', strict_slashes=False)
def mvp():
    """First mvp"""
    all_products = storage.all(Product).values()
    all_products = sorted(all_products, key=lambda k: k.name)
    list_products = []

    for product in all_products:
        list_products.append([product])

    categories = storage.all(Category).values()
    categories = sorted(categories, key=lambda k: k.name)

    products = storage.all(Product).values()
    products = sorted(products, key=lambda k: k.name)

    return render_template('ecommerce.html',
                           products=products,
                           categories=categories)


if __name__ == "__main__":
    host = environ.get('API_HOST')
    port = environ.get('API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
#    load_dotenv()
    app.run(host=host, port=port, threaded=True, debug=True)
