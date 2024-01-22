import tweepy as TP
from .Secrets import twitter_SECRETS as TS

def handle_user():
    oauth2_user_handler = TP.OAuth2UserHandler(
        client_id=TS.CLIENT_ID,
        redirect_uri=TS.REDIRECT_URI,
        scope=['tweet.read', 'tweet.write', 'users.read']
    )

    return oauth2_user_handler.get_authorization_url()