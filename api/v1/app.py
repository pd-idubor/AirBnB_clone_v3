#!/usr/bin/python3
"""
    Methods
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(exception):
    """Closes the current session"""
    storage.close()


if __name__ == "__main__":
    app_host = os.getenv('HBNB_API_HOST')
    app_port = os.getenv('HBNB_API_PORT')
    if (app_host is None):
        app_host = '0.0.0.0'

    if (app_port is None):
        app_port = 5000

    app.run(host=app_host, port=int(app_port), threaded=True)
