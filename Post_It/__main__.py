from flask import Flask, request, render_template, redirect
import os

import app.Twitter.twitter as TT
import app.Twitter.login_twitter as TL
import tweepy as TP

twitter = False
facebook = False
instagram = False
telegram = False
furaffinity = False

redirect_url = ''

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

def create_app():
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            if request.form['twitter_login'] == 'login_with_twitter':
                twitter = True
                print('oi')
                redirect_url = TL.twitter_redirect()
                return redirect(redirect_url, 302)
            else:
                pass # unkno
        return render_template('index.html')
    return app

@app.route('/twitter_login', methods=['GET', 'POST'])
def receive_twitter_tokens():
    auth = TL.apply_verifier(request.form['oauth_verifier'])
    if auth:
        api = TP.API(auth)
        print(api.auth)
        #NOTE: After authentication api.auth will be a tuple with both access_token and access_secret
        #TODO: Save Token and Secret to Secrets/ in a JSON file
    return redirect('/', 302)



create_app() 
app.run(host="localhost", port=8080, debug=True)
