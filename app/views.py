"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    views.py : Magic happens here :)
"""

from flask import render_template
from flask import jsonify
from app import app

from twitter import Twitter

DEFAULT_HASHTAG = 'custserv'

@app.route('/')
@app.route('/index')
def index():
    try:
        twitter_obj = Twitter()
        fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(DEFAULT_HASHTAG))
        return render_template('index.html',
                               fetched_tweets=fetched_tweets)
    except Exception as error:
        print error

@app.route('/api/get-json')
def default_tweet_json():
    twitter_obj = Twitter()
    fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(DEFAULT_HASHTAG))
    return jsonify(fetched_tweets)


@app.route('/api/tweets/<hash_tag>')
def get_hashtag_tweets(hash_tag):
    twitter_obj = Twitter()
    fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(hash_tag))
    return render_template('index.html',
                           fetched_tweets = fetched_tweets)


@app.route('/api/tweets/get-json/<hash_tag>')
def get_hashtag_tweets_json(hash_tag):
    twitter_obj = Twitter()
    fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(hash_tag))
    return jsonify(fetched_tweets)





