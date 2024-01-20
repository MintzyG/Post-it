import tweepy as TP
from Secrets import Twitter_SECRETS as TS

def Twitter_Post():
    api = TP.Client(TS.BEARER_TOKEN, TS.API_KEY, TS.API_SECRET, TS.CLIENT_ID, TS.CLIENT_SECRET)
    auth = TP.OAuth1UserHandler(TS.CLIENT_ID, TS.CLIENT_SECRET, TS.API_KEY, TS.API_SECRET)
    oldapi = TP.API(auth)
    media1 = oldapi.media_upload("img1.jpg")
    api.create_tweet(text='I love my boyfriend :3',media_ids=[media1.media_id])

Twitter_Post()