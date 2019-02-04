#!/usr/bin/python3
"""Import blueprint, create a variable which is an instance of blueprint"""
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
