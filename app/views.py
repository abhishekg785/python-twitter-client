"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    views.py : The logic goes here
"""

from app import app

# Index route
@app.route('/')
@app.route('/index')
def index():
    print "hello world"