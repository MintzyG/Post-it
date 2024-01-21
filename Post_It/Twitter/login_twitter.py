import os 
print(os.getcwd())
from .Secrets import twitter_SECRETS as TS
import tweepy as TP 
import requests as REQ

def get_twitter_auth():
    auth = TP.OAuthHandler(TS.CONSUMER_KEY, TS.CONSUMER_SECRET, 'https://localhost:8080')
    try:
        redirect_url = auth.get_authorization_url()
        print(f'Please go to {redirect_url}.')
    except:
        print('Error! Failed to get request token.') 
        
    #TODO: spin up a web server to get the oauth_token and oauth_verifier
    verifier = input('verifier: ')

    try: 
        return auth.get_access_token(verifier)
    except:
        print('failed to get acess token')
        return None
    
def main():
    auth = get_twitter_auth()
    if auth:
        api = TP.API(auth)
        #NOTE: After authentication api.auth will be a tuple with both access_token and access_secret
        #TODO: Save Token and Secret to Secrets/ in a JSON file

if __name__ == "__main__":
    main()



