import os 
print(os.getcwd())
from .Secrets import twitter_SECRETS as TS
import tweepy as TP 
from requests import request, session



def get_twitter_auth():
    auth = TP.OAuthHandler(TS.CONSUMER_KEY, TS.CONSUMER_SECRET)
    try:
        redirect_url = auth.get_authorization_url()
        print(f'Please go to {redirect_url}.')
    except:
        print('Error! Failed to get request token.') 
        
    
    verifier = input('Verifier:')

    try: 
        auth.get_access_token(verifier)
    except:
        print('failed to get acess token')
        return None
    
def main():
    auth = get_twitter_auth()
    if auth:
        api = TP.api(auth)

        user = api.me()
        print(f'Autenticated as {user.screen_name}')
        print(f'Acess token: {auth.acess.token}')
        print(f'Acess token Secret: {auth.access_token_secret}')

if __name__ == "__main__":
    main()



