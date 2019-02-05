#!/usr/bin/python3
""" new State object view. Handles default RESTful API actions"""
from flask import Flask
from flask import jsonify
from flask import abort
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'])
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


