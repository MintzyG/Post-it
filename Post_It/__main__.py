from flask import Flask, render_template
import os

import app.Twitter.twitter as TT
import app.Twitter.login_twitter as TL

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

def create_app():
    @app.route('/')
    def home():
        return render_template('index.html')
   
    return app

create_app()
app.run(host="localhost", port=8080, debug=True)

if __name__ == "__main__":
        twitter = True
        facebook = False
        instagram = False
        telegram = False
        furaffinity = False

        if twitter:
            TT.twitter_post()
            TL.main()
        elif facebook:
            pass
        elif instagram:
            pass
        elif telegram:
            pass
        elif furaffinity:
            pass