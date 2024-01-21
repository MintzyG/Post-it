from flask import Flask, request, render_template
import os

import app.Twitter.twitter as TT
import app.Twitter.login_twitter as TL

twitter = False
facebook = False
instagram = False
telegram = False
furaffinity = False

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

def create_app():
    @app.route('/')
    def home():
        if request.method == 'POST':
            if request.form['twitter_login'] == 'login_with_twitter':
                twitter = True
                print('oi')
                TL.twitter_login()
            else:
                pass # unknown
        return render_template('index.html')
   
    return app

create_app()
app.run(host="localhost", port=8080, debug=True)
