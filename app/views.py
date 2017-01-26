"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    views.py : Magic happens here :)
"""

from flask import render_template
from flask import jsonify

from app import app

""" My self created Twitter class to handle the Twitter oauth 
and fetching of the tweets for a particular hashTag and which have
been re-Tweeted atleast once
"""
from twitter import Twitter

DEFAULT_HASHTAG = 'custserv'    # The default hashtag as given in the task

@app.route('/')
@app.route('/index')
def index():
    """ Fetches the Tweets for the DEFAULT_HASHTAG using the imported Twitter class
    Returns the index.html template along with the fetched tweets list 
    which can be rendered in the template at the client side

    ::
        GET /
        GET /index

    """
    try:
        twitter_obj = Twitter()
        fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(DEFAULT_HASHTAG))
        return render_template('index.html',
                               fetched_tweets=fetched_tweets)
    except Exception as error:
        print error


@app.route('/api/default')
def default_tweet_json():
    """ Fetches the Tweets for the DEFAULT_HASHTAG using the imported Twitter class
    Returns the json for the fetched tweets as a response 

    ::
        GET /api/default

    Sample Response
    ^^^^^^^^^^^^^^^

    ::
        {
          "fetched_tweets": [
            {
              "contributors": null, 
              "coordinates": null, 
              "created_at": "Thu Jan 26 13:31:27 +0000 2017", 
              "entities": {
                "hashtags": [
                ], 
                "symbols": [], 
                "urls": [
                ], 
                "user_mentions": [
                ]
              }, 
              "favorite_count": 0, 
              "favorited": false, 
              "geo": null, 
              "id": 824610707689840640, 
              "id_str": "824610707689840640", 
              "in_reply_to_screen_name": null, 
              "in_reply_to_status_id": null, 
              "in_reply_to_status_id_str": null, 
              "in_reply_to_user_id": null, 
              "in_reply_to_user_id_str": null, 
              "is_quote_status": false, 
              "lang": "en"
              ...
            },
            {
            ...
        }

    """
    try:
        twitter_obj = Twitter()
        fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(DEFAULT_HASHTAG))
        return jsonify({
            'fetched_tweets' : fetched_tweets
        })
    except Exception as error:
        print error


@app.route('/api/tweets/<hash_tag>')
def get_hashtag_tweets(hash_tag):
    """ Fetches the Tweets for a particular hash_tag using the imported Twitter class
    Returns the index.html template along with the fetched tweets list 
    which can be rendered in the template at the client side

    ::
        GET /api/tweets/<hash_tag>

    """
    try:
        twitter_obj = Twitter()
        fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(hash_tag))
        return render_template('index.html',
                               fetched_tweets = fetched_tweets)
    except Exception as error:
        print error


@app.route('/api/tweets/get-json/<hash_tag>')
def get_hashtag_tweets_json(hash_tag):
    """ Fetches the Tweets for a particular hash_tag using the imported Twitter class
    Returns the json for the fetched tweets as a response

    ::
        /api/tweets/get-json/<hash_tag>

    Sample Response
    ^^^^^^^^^^^^^^^

    /api/tweets/get-json/anonymous
    ::
        {
          "fetched_tweets": [
            {
              "contributors": null,
              "coordinates": null,
              "created_at": "Thu Jan 26 13:54:27 +0000 2017",
              "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                ]
              },
              "favorite_count": 0,
              "favorited": false,
              "geo": null,
              "id": 824616493535027204,
              "id_str": "824616493535027204",
              "in_reply_to_screen_name": null,
              "in_reply_to_status_id": null,
              "in_reply_to_status_id_str": null,
              "in_reply_to_user_id": null,
              "in_reply_to_user_id_str": null,
              "is_quote_status": false,
              "lang": "en",
              "metadata": {
                "iso_language_code": "en",
                "result_type": "recent"
              },
              "place": null,
              "retweet_count": 1,
              "retweeted": false,
              "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Thu Jan 26 11:54:07 +0000 2017",
                "entities": {
                  "hashtags": [],
                  "symbols": [],
                  "urls": [],
                  "user_mentions": []
                },
                "favorite_count": 1,
                "favorited": false,
                "geo": null,
                "id": 824586211683561472,
                "id_str": "824586211683561472",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                ...
                }
              },
              {
              ...
        }

    """
    try:
        twitter_obj = Twitter()
        fetched_tweets = twitter_obj.fetch_hashtag_tweets(str(hash_tag))
        return jsonify({
            'fetched_tweets' : fetched_tweets
        })
    except Exception as error:
        print error





