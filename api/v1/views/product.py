#!/usr/bin/python3
"""objects that handle all default restful api actions for states"""
from models.product import Product
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
    """
    Retrieves the list of states
    """
    all_products = storage.all(Product).values()
    list_products = []
    for product in all_products:
        list_products.append(product.to_dict())
    return jsonify(list_products)


@app_views.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
    """Retrieve a specific product"""
    product = storage.get(Product, product_id)
    if not product:
        abort(404)
    return jsonify(product.to_dict())


@app_views.route('/products/category/<category_id>', methods=['GET'], strict_slashes=False)
def get_product_bycategory(category_id):
    """Retrieve a specific product depending of a class"""
    all_products = storage.all(Product).values()
    list_products = []
    for product in all_products:
        if str(product.to_dict()["category"]) == str(category_id):
            list_products.append(product.to_dict())
    return jsonify(list_products)


# @app_views.route('/products_search', methods=['POST'], strict_slashes=False)
def get_product_search():
    """Retrieve a specific product depending of a class"""
    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()
    if data and len(data):
        categories = data.get('categories', None)

    if not data or not len(data) or (not categories):
        products = storage.all(Product).values()
        list_products = []
        for product in products:
            list_products.append(product.to_dict())
        return jsonify(list_products)

    list_products = []
    if categories:
        if not list_products:
            list_products = storage.all(Product).values()
        categories_obj = [storage.get(Category, cid) for cid in categories]
        list_products = []
    for product in all_products:
        if str(product.to_dict()["category"]) == str(category_id):
            list_products.append(product.to_dict())
    return jsonify(list_products)
