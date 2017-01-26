"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    __init__.py : Application starts here
"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views  # Imported at the end as views depends on the app, to prevent circular import
