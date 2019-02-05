#!/usr/bin/python3
""" new State object view. Handles default RESTful API actions"""
from flask import Flask
from flask import jsonify
from flask import abort
from api.v1.views import app_views
from models import storage
from flask import request
import jsonify

@app_views.route('/states', methods=['GET'], strict_slashes = False)
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

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id=None):
    state = storage.get("State", state_id)
    print(state)
    if state is None:
        abort(404)
    else:
        storage.delete(state)
        storage.save()
        return jsonify({}), 200

@app_views.route('/api/v1/states', methods=['POST'])
def post_state():
    data = request.get_json()
    if not data.validate():
        abort(400, 'Not a JSON')
    if name not in data:
        abort(400, 'Missing name')
    return jsonify(data), 201


