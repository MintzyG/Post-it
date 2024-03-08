import tweepy as TP
import os, sys, json

from .check_twitter_login import check_login_state

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from secrets import twitter_api_credentials as TS
from helpers.check_empty_file import check_file

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

def post(CK, CS, AT, AS):
    media_paths = []
    media_id = []

    client_v1 = get_v1_conn(CK, CS, AT, AS)
    client_v2 = get_v2_conn(CK, CS, AT, AS)
    
    #TODO: Implement this on the GUI
    with open('./Post_It/temp/images.json', "r") as fp:
        paths = json.load(fp)

    for pictures in paths['images']:
        media_paths.append(pictures)
        print(pictures)
    
    if len(media_paths) > 4:
        raise ValueError
    
    for media_path in media_paths:
        media = client_v1.media_upload(filename=media_path) 
        media_id.append(media.media_id)
    
    media_id_strs = [str(id) for id in media_id]
    try: client_v2.create_tweet(text=os.getenv('BODY'), media_ids=media_id_strs) 
    except: print('fuck') #TODO: Implement warning for GUI

def twitter_post():
    try:
        if check_file(os.getenv('TWITTER_SECRET_JSON')):
            with open(os.getenv('TWITTER_SECRET_JSON'), 'r') as fp:
                data = json.load(fp)
                AT = data['ACCESS_TOKEN']
                AS = data['ACCESS_SECRET']
            fp.close()
        else:
            raise UnboundLocalError
    except:
        print('Não está logado para postar')
            
    CK = TS.CONSUMER_KEY
    CS = TS.CONSUMER_SECRET
    
    check_login_state()
    print('everything ready to post!')
    try: post(CK=CK, CS=CS, AT=AT, AS=AS) 
    except: print(f"Images exceed the maximum limit of 4.")
        