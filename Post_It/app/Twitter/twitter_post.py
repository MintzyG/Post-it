import tweepy as TP
import os, json
from .Secrets import twitter_SECRETS as TS
from .check_twitter_login import check_login_state
from ..helper_functions.check_empty_file import check_file

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
    #TODO: Implement this on the GUI    
    os.environ['BODY'] = 'Meu texto do meu post'    

def post(CK, CS, AT, AS):
    client_v1 = get_v1_conn(CK, CS, AT, AS)
    client_v2 = get_v2_conn(CK, CS, AT, AS)
    #TODO: Implement this on the GUI
    media_paths = ["./img1.jpg", "./img2.jpg", "./img3.jpg", "./img4.jpg", "./img5.jpg"]
    media_id = []
    if len(media_paths) > 4:
        raise ValueError
    for media_path in media_paths:
        print(os.getcwd())
        print(media_path)
        media = client_v1.media_upload(filename=media_path) 
        media_id.append(media.media_id)
    media_id_strs = [str(id) for id in media_id]
    try: client_v2.create_tweet(text=os.getenv('BODY'), media_ids=media_id_strs) 
    except: pass #TODO: Implement warning for GUI

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
    
    
    check_login_state(AT=AT, AS=AS)
    get_text()
    try: post(CK=CK, CS=CS, AT=AT, AS=AS) 
    except: print(f"Images exceed the maximum limit of 4.")
        