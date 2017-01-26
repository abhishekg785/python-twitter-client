"""
    author : abhishek goswami ( Hiro )
    abhishekg785@gmail.com

    Twitter.py
    Creates an oauth connection with the Twitter using credentials from config.py
    Fetches the twitter data
"""

from app import app

""" Required by the Twitter class
OAuthHandler is required for handling oauth since Twitter API1.1
requires oAuth
"""
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

import json


class Twitter():

    def __init__(self):
        """ Sets the app credentials fetched from the config
        Call the OAuthHandler and API function to authenticate the user credentials
        app.config have been set in the __init__.py file.
        app.config contains the twitter app credentials.
        """ 

        self.MAX_TWEETS = 50    # Max no of tweets to be fetched at a time
        self.fetched_tweets_list = []   # List of the fetched tweets

        try:
            consumer_key = app.config['CONSUMER_KEY']
            consumer_secret = app.config['CONSUMER_SECRET']
            access_token_key = app.config['ACCESS_TOKEN_KEY']
            access_token_secret = app.config['ACCESS_TOKEN_SECRET']
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token_key, access_token_secret)
            self.api = API(self.auth, wait_on_rate_limit=True)
            print 'Successfully Authenticated :) '
        except Exception as error:
            print 'Error Occurred !'
            print error


    def fetch_hashtag_tweets(self, hashtag_str):
        """ Fetches the tweets for a particular hashTag

        :param hashtag_str: The hashTag for which the tweets have to be fetched
        :return: The list of the fetched tweets for the hashtag where each item is a tweet JSON
        """
        try:
            print 'Fetching tweets for the #' + hashtag_str
            fetched_tweets = Cursor(self.api.search, q = str(hashtag_str)).items(self.MAX_TWEETS)
            for tweet in fetched_tweets:
                tweet_json = json.loads(json.dumps(tweet._json))
                # Getting the re-Tweet count of the tweet
                re_tweet_count = tweet_json['retweet_count']
                # For getting tweets that have been retweeted more than once
                if re_tweet_count > 0:                               
                    self.fetched_tweets_list.append(tweet_json)
            return self.fetched_tweets_list
        except Exception as error:
            print error