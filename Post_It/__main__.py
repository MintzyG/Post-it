from flask import Flask, request, render_template, redirect
import os, json

import app.Twitter.twitter_post as TT
import app.Twitter.login_twitter as TL
import tweepy as TP
import app.Twitter.Secrets.twitter_SECRETS as TS
from app.Twitter.check_twitter_login import check_login_state
from app.helper_functions.check_empty_file import check_file

twitter = False
facebook = False
instagram = False
telegram = False
furaffinity = False

os.environ['TWITTER_SECRET_JSON'] = './Post_It/app/Twitter/Secrets/twitter_credentials.json' 

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

def create_app():
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            if request.form['twitter_login'] == 'login_with_twitter':
                global authorization_url, oauth1
                tuple = TL.handle_user()
                authorization_url = tuple[0]
                oauth1 = tuple[1]
                return redirect(authorization_url, 302)
        return render_template('index.html')
    return app

@app.route('/twitter_login', methods=['GET', 'POST'])
def finalize_login():
    token = request.args.get('oauth_verifier')
    access_token, access_secret = oauth1.get_access_token(token)
    twitter_credentials = {
        'ACCESS_TOKEN' : access_token,
        'ACCESS_SECRET' : access_secret
    }
    twitter_login_state = check_login_state()

    if not twitter_login_state:
        with open(os.getenv('TWITTER_SECRET_JSON'), 'w') as fp:
            json.dump(twitter_credentials, fp)
        fp.close()
    
    twitter_login_state = check_login_state()

    return redirect('/', 302)

try:
    with open(os.getenv('TWITTER_SECRET_JSON'), 'x') as fp:
        pass
    fp.close()
except:
    pass    


create_app() 
app.run(host="127.0.0.1", port="443", debug=True)
