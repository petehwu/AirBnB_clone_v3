#!/usr/bin/python3


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """returns a json ok string
    """
    return jsonify({"status": "OK"})
