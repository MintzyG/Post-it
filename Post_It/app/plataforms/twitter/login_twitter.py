import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from secrets import twitter_api_credentials as TS

import tweepy as TP

def handle_user():
    oauth1_user_handler = TP.OAuth1UserHandler(
        TS.CONSUMER_KEY,
        TS.CONSUMER_SECRET,
        TS.REDIRECT_URI
    )
    return (oauth1_user_handler.get_authorization_url(signin_with_twitter=True), oauth1_user_handler)