#!/usr/bin/python3
"""
start flask app; register the blueprint app_views to app,
also define a teardown mothode
"""
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_methode(args):
    """
    close the sqlAlchemy session by calling close the methode on storage.
    """
    storage.close()


@app.errorhandler(404)
def not_found_page(err):
    """ handling not found page """
    return jsonify(error="Not found"), 404


if __name__ == '__main__':
    API_host = getenv('HBNB_API_HOST') or "0.0.0.0"
    API_port = int(getenv("HBNB_API_PORT") or 5000)
    app.run(host=API_host, port=API_port, threaded=True)
