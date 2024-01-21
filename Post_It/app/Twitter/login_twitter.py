import os 
print(os.getcwd())
from .Secrets import twitter_SECRETS as TS
import tweepy as TP 
import requests as REQ
from flask import Flask, redirect

def apply_verifier(code: str):
    auth = TP.OAuthHandler(TS.CONSUMER_KEY, TS.CONSUMER_SECRET, 'https://localhost:8080/twitter_login')
    #TODO: spin up a web server to get the oauth_token and oauth_verifier
    #verifier = input('verifier: ')
    verifier = code
    try: 
        return auth.get_access_token(verifier)
    except:
        print('failed to get acess token')
        return None
    
def twitter_redirect():
    auth = TP.OAuthHandler(TS.CONSUMER_KEY, TS.CONSUMER_SECRET, 'https://localhost:8080/twitter_login')
    try:
        #TODO: make redirect work
        redirect_url = auth.get_authorization_url()
        print(redirect_url)
        return redirect_url
    except:
        print('Error! Failed to get request token.')   
    
   