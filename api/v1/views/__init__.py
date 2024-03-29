#!/usr/bin/python3
"""
create an instance of blueprint class to with url_prefix
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")

from api.v1.views.index import *
