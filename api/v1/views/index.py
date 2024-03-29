#!/usr/bin/python3
"""
Create an endpoint that return a json object that have
the status of our API
"""
from api.v1.views import app_views
from flask import jsonify
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app_views.route('/status', strict_slashes=False)
def status():
    """
    return the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stast():
    """ return a Json for all classes and their count"""
    count_dict = {}
    for key in classes.keys():
        count_dict[key] = models.storage.count(key)
    return jsonify(count_dict)
