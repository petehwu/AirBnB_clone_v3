#!/usr/bin/python3
""" new State object view. Handles default RESTful API actions"""
from flask import Flask
from flask import jsonify
from flask import abort
from api.v1.views import app_views
from models import storage
from flask import request
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id=None):
    states = [state.to_dict() for state in storage.all("State").values()]
    if state_id is None:
        return jsonify(states)
    else:
        obj = storage.get("State", state_id)
        if obj is None:
            abort(404)
        return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id=None):
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    state = State()
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'name' not in data.keys():
            abort(400, 'Missing name')
    for key, value in data.items():
        setattr(state, key, value)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id=None):
    state = storage.get("State", state_id)
    data = request.get_json()
    if state is None:
        abort(404)
    print("STATE: {}".format(state))
    if data is None:
        abort(400, "Not a JSON")
    else:
        for key, value in data.items():
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
