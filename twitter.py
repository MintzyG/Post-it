import tweepy as TP
from Secrets import Twitter_SECRETS as TS

CK = TS.CONSUMER_KEY
CS = TS.CONSUMER_SECRET
AT = TS.ACCESS_TOKEN
AS = TS.ACCESS_SECRET

def get_v1_conn(CK, CS, AT, AS) -> TP.API:
    auth = TP.OAuth1UserHandler(CK, CS)
    auth.set_access_token(AT, AS)
    return TP.API(auth)

def get_v2_conn(CK, CS, AT, AS) -> TP.Client:
    client = TP.Client(
        consumer_key=CK, consumer_secret=CS,
        access_token=AT, access_token_secret=AS
    )
    return client

def Twitter_Post():
    client_v1 = get_v1_conn(CK, CS, AT, AS)
    client_v2 = get_v2_conn(CK, CS, AT, AS)
    media_path = "./img1.jpg"
    media = client_v1.media_upload(filename=media_path)
    media_id = media.media_id
    client_v2.create_tweet(text='I love my boyfriend :3', media_ids=[media_id])

Twitter_Post()