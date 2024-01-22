import tweepy as TP
from .Secrets import twitter_SECRETS as TS

def handle_user():
    oauth1_user_handler = TP.OAuth1UserHandler(
        TS.CONSUMER_KEY,
        TS.CONSUMER_SECRET,
        TS.REDIRECT_URI
    )
    return (oauth1_user_handler.get_authorization_url(signin_with_twitter=True), oauth1_user_handler)