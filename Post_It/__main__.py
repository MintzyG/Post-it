from flask import Flask, request, render_template, redirect
import os

import app.Twitter.twitter as TT
import app.Twitter.login_twitter as TL
import tweepy as TP
import app.Twitter.Secrets.twitter_SECRETS as TS

twitter = False
facebook = False
instagram = False
telegram = False
furaffinity = False

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
    print(access_token)
    print(access_secret)
    return redirect('/', 302)

create_app() 
app.run(host="127.0.0.1", port="443", debug=True)
