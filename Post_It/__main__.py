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
                global redirect_url
                redirect_url = TL.handle_user()
                print(redirect_url)
                return redirect(redirect_url, 302)
        return render_template('index.html')
    return app

@app.route('/twitter_login', methods=['GET', 'POST'])
def finalize_login():
    url = request.url
    print(url)
    access_token = TP.OAuth2UserHandler.fetch_token(url)
    print(access_token)
    return redirect('/', 302)

create_app() 
app.run(host="127.0.0.1", port="443", debug=True)
