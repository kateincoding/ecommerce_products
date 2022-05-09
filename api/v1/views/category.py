#!/usr/bin/python3
"""objects that handle all default restful api actions for states"""
from models.category import Category
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """
    Retrieves the list of states
    """
    all_categories = storage.all(Category).values()
    list_categories = []
    for category in all_categories:
        list_categories.append(category.to_dict())
    return jsonify(list_categories)
