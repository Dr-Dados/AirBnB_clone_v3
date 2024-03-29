#!/usr/bin/python3
"""
start flask app
"""
from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_methode(args):
    """
    close the storage variable
    """
    storage.close()


if __name__ == '__main__':
    API_host = getenv('HBNB_API_HOST') or "0.0.0.0"
    API_port = int(getenv("HBNB_API_PORT") or 5000)
    app.run(host=API_host, port=API_port, threaded=True)
