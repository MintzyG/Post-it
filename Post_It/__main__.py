from flask import Flask, request, render_template, redirect
import tweepy as TP
import os, json

import app.Twitter.Secrets.twitter_SECRETS as TS
import app.Twitter.login_twitter as TL
import app.Twitter.twitter_post as TT
from app.Twitter.check_twitter_login import check_login_state
from app.helper_functions.check_empty_file import check_file
from app.select_images import select_images

os.environ['TWITTER_SECRET_JSON'] = './Post_It/app/Twitter/Secrets/twitter_credentials.json' 

app = Flask(__name__,
            static_folder="app/static",
            template_folder="app/templates")

def create_app():
    @app.route('/')
    def home():
        return render_template('index.html')
    return app

@app.route('/', methods=['POST'])
def process_form():
    print(request.method)
    global redirect_url
    global redirect_user
    global handles

    if request.method == 'POST':
        Button_handler()       
        if redirect_user:
            redirect_user = False
            return redirect(redirect_url, 302)
    return render_template('index.html')

@app.context_processor
def inject_dictionary():
    global handles
    return dict(handles=handles)

@app.route('/twitter_login', methods=['GET', 'POST'])
def finalize_login():
    print(request.method)
    token = request.args.get('oauth_verifier')
    access_token, access_secret = oauth1_twitter.get_access_token(token)
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

def Button_handler():
    global twitter
    global facebook    
    global instagram  
    global telegram   
    global furaffinity 
    global redirect_user
    global handles

    if request.form.get('twitter_toggle') == 'twitter_toggle':
        twitter = not twitter
        print(f'Twitter state {twitter}')
        handles['twitter_toggle'] = twitter
    elif request.form.get('instagram_toggle') == 'instagram_toggle':
        instagram = not instagram
        print(f'instagram state {instagram}')
        handles['instagram_toggle'] = instagram
    elif request.form.get('facebook_toggle') == 'facebook_toggle':
        facebook = not facebook
        print(f'facebook state {facebook}')
        handles['facebook_toggle'] = facebook
    elif request.form.get('furaffinity_toggle') == 'furaffinity_toggle':
        furaffinity = not furaffinity
        print(f'furaffinity state {furaffinity}')
        handles['furaffinity_toggle'] = twitter
    elif request.form.get('telegram_toggle') == 'telegram_toggle':
        telegram = not telegram
        print(f'telegram state {telegram}')
        handles['telegram_toggle'] = telegram

    elif request.form.get('twitter_login') == 'twitter_login' and twitter:
        global redirect_url, oauth1_twitter
        tuple = TL.handle_user()
        redirect_url = tuple[0]
        oauth1_twitter = tuple[1]
        redirect_user = True
        return
    elif request.form.get('instagram_login') == 'instagram_login' and instagram:
        pass
    elif request.form.get('facebook_login') == 'facebook_login' and facebook:
        pass
    elif request.form.get('furaffinity_login') == 'furaffinity_login' and furaffinity:
        pass
    elif request.form.get('telegram_login') == 'telegram_login' and telegram:
        pass

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
        #Generalize posting
        texto = request.form.get('input_text')
        os.environ['BODY'] = texto
        print(f'That`s your text: {str(texto)}')
        try:
            if handles['twitter_toggle']:
                TT.twitter_post()
            if handles['instagram_toggle']:
                pass
            if handles['facebook_toggle']:
                pass
            if handles['furaffinity_toggle']:
                pass
            if handles['telegram_toggle']:
                pass
        except:
            print('Não foi postado')
            return render_template('index.html')
        try:
            del os.environ['BODY']
            os.remove('./Post_It/temp/images.json')       
        except:
            print('File already deleted')

def init():
    global twitter
    global facebook    
    global instagram  
    global telegram   
    global furaffinity 
    global redirect_user
    global redirect_url
    global handles 

    handles = {
        'twitter_toggle': bool,
        'instagram_toggle': bool,
        'facebook_toggle': bool,
        'furaffinity_toggle': bool,
        'telegram_toggle': bool
    }

    twitter = False
    facebook = False
    instagram = False
    telegram = False
    furaffinity = False
    redirect_user = False
    redirect_url  = None

try:
    with open(os.getenv('TWITTER_SECRET_JSON'), 'x') as fp:
        pass
    fp.close()
except:
    pass    

if os.path.isfile('./Post_It/temp/images.json'):
    os.remove('./Post_It/temp/images.json')

init()
create_app() 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="443", debug=True)