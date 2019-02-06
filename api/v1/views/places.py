#!/usr/bin/python3
"""This is the flask file for places"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User


@app_views.route('/cities/<city_id>/places',
                 strict_slashes=False, methods=['GET'])
def show_city_place(city_id):
    """This method shows all places for a city
    """
    city = storage.get("City", city_id)
    if city:
        return jsonify([p.to_dict() for p in city.places])
    else:
        abort(404)


@app_views.route('/places/<place_id>',
                 strict_slashes=False, methods=['GET'])
def show_place(place_id):
    """ This method shows the place based on id
    """
    p = storage.get("Place", place_id)
    if p:
        return jsonify(p.to_dict())
    else:
        abort(404)


@app_views.route('/places/<place_id>',
                 strict_slashes=False, methods=['DELETE'])
def delete_place(place_id):
    """This method deletes a place
    """
    p = storage.get("Place", place_id)
    if p:
        storage.delete(p)
        storage.save()
        return(jsonify({}), 200)
    else:
        abort(404)


@app_views.route('/cities/<city_id>/places',
                 strict_slashes=False, methods=['POST'])
def create_place(city_id):
    """This method creates a new place
    """
    vals = request.get_json(silent=True)
    city = storage.get("City", city_id)
    if city is None:
        abort(404)
    if vals is None:
        abort(400, "Not a JSON")
    if "user_id" not in vals:
        abort(400, "Missing user_id")
    if "name" not in vals:
        abort(400, "Missing name")
    if "city_id" not in vals:
        vals["city_id"] = city_id
    user = storage.get("User", vals.get("user_id"))
    if user is None:
        abort(404)
    p = Place()
    for k, v in vals.items():
        setattr(p, k, v)
    storage.new(p)
    storage.save()
    return (jsonify(p.to_dict()), 201)


@app_views.route('/places/<place_id>',
                 strict_slashes=False, methods=['PUT'])
def update_place(place_id):
    """This method updates the place
    """
    p = storage.get("Place", place_id)
    vals = request.get_json(silent=True)
    if vals is None:
        abort(400, "Not a JSON")
    if p is None:
        abort(404)
    for k, v in vals.items():
        if k not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(p, k, v)
    storage.save()
    return(jsonify(p.to_dict()), 200)
