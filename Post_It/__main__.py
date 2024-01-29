from flask import Flask, request, render_template, redirect
import tweepy as TP
import os, json

import app.Twitter.twitter_post as TT
import app.Twitter.login_twitter as TL

import app.Twitter.Secrets.twitter_SECRETS as TS

from app.Twitter.check_twitter_login import check_login_state

from app.helper_functions.check_empty_file import check_file

from app.select_images import select_images

twitter = False
facebook = False
instagram = False
telegram = False
furaffinity = False

os.environ['TWITTER_SECRET_JSON'] = './Post_It/app/Twitter/Secrets/twitter_credentials.json' 

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

#TODO: make a post button
def create_app():
    @app.route('/')
    def home():
        return render_template('index.html')
    return app

@app.route('/', methods=['POST'])
def process_form():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('twitter_login') == 'login_with_twitter':
            global authorization_url, oauth1
            tuple = TL.handle_user()
            authorization_url = tuple[0]
            oauth1 = tuple[1]
            return redirect(authorization_url, 302)
    
        elif request.form.get('select_image') == 'select_image':
            images = select_images()
            try:
                if os.path.isfile('./Post_It/temp/images.json'):
                    os.remove('./Post_It/temp/images.json')
                with open('./Post_It/temp/images.json', 'w') as fp:
                    print(images)
                    json.dump(images, fp)
                fp.close()
            except:
                print('Deu não')
        
        elif request.form.get('post') == 'post':
            texto = request.form.get('input_text')
            os.environ['BODY'] = texto
            print(f'That`s your text: {str(texto)}')
            try:
                TT.twitter_post()
            except:
                print('Não foi postado')
                return render_template('index.html')
            try:
                del os.environ['BODY']
                os.remove('./Post_It/temp/images.json')       
            except:
                print('File already deleted')

    return render_template('index.html')

@app.route('/twitter_login', methods=['GET', 'POST'])
def finalize_login():
    print(request.method)
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

if os.path.isfile('./Post_It/temp/images.json'):
    os.remove('./Post_It/temp/images.json')

create_app() 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="443", debug=True)