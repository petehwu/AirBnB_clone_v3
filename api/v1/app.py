#!/usr/bin/python3
"""Returns the status of the API"""
from flask import Flask
from models import storage
from api.v1.views import app_views

app = flask.Flask(__name__)

app_views = register_blueprint(app_views)

@app.teardown_appcontext
def storage_close(value):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True)
