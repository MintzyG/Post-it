import tweepy as TP
import os
from Secrets import Twitter_SECRETS as TS
from Post_It.check_login import check_login_state

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

def get_text():
    os.environ['BODY'] = 'Meu texto do meu post'    

def post(CK, CS, AT, AS):
    client_v1 = get_v1_conn(CK, CS, AT, AS)
    client_v2 = get_v2_conn(CK, CS, AT, AS)
    media_paths = ["./img1.jpg", "./img2.jpg", "./img3.jpg", "./img4.jpg", "./img5.jpg"]
    media_id = []
    for media_path in media_paths:
        print(os.getcwd())
        print(media_path)
        media = client_v1.media_upload(filename=media_path) 
        media_id.append(media.media_id)
    media_id_strs = [str(id) for id in media_id]
    try: client_v2.create_tweet(text=os.getenv('BODY'), media_ids=media_id_strs) 
    except: pass #TODO: Implement warning for GUI

def twitter_post():
    CK = TS.CONSUMER_KEY
    CS = TS.CONSUMER_SECRET
    AT = TS.ACCESS_TOKEN
    AS = TS.ACCESS_SECRET

    check_login_state(AT=AT, AS=AS)
    get_text()
    post(CK=CK, CS=CS, AT=AT, AS=AS)