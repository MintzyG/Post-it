import sys
import os, json
from flask import Flask, request, render_template, redirect, Blueprint

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Secrets import twitter_api_credentials as TS
from app.plataforms.twitter.check_twitter_login import check_login_state

import tweepy as TP

def handle_user():
    oauth1_user_handler = TP.OAuth1UserHandler(
        TS.CONSUMER_KEY,
        TS.CONSUMER_SECRET,
        TS.REDIRECT_URI
    )
    return (oauth1_user_handler.get_authorization_url(signin_with_twitter=True), oauth1_user_handler)


import __main__
login_twitter_final = Blueprint('login_twitter_final', __name__, template_folder='templates')
@login_twitter_final.route('/twitter_login', methods=['GET', 'POST'])
def finalize_twitter_login():
    print(request.method)
    secret_path = os.getenv('TWITTER_SECRET_JSON')
                            
    token = request.args.get('oauth_verifier')
    access_token, access_secret = __main__.oauth1_twitter.get_access_token(token)
    twitter_credentials = {
        'ACCESS_TOKEN' : access_token,
        'ACCESS_SECRET' : access_secret
    } 

    try:
        if os.path.isfile(secret_path):
            os.remove(secret_path)
            open(secret_path, 'x+').close()
    except:
        pass
    
    twitter_login_state = check_login_state()
    
    if not twitter_login_state:
        with open(secret_path, 'w') as fp:
            json.dump(twitter_credentials, fp)
        fp.close()
    twitter_login_state = check_login_state()
    return redirect('/', 302)