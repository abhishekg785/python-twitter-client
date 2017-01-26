"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    __init__.py : Application starts here
"""

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)

""" For enabling Cross Domain Request
"""
CORS(app)

""" Set the config file to app for later use
config consist of the twitter app credentials
"""
app.config.from_object('config')

""" Views have been imported at the last as it is
dependent on the app and to prevent circular import
"""
from app import views
