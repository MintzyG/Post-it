from flask import Flask, request, render_template, redirect
import tweepy as TP
import os, json

import Secrets.twitter_api_credentials as TS
import app.plataforms.twitter.login_twitter as TL
import app.plataforms.twitter.twitter_post as TT
from app.plataforms.twitter.check_twitter_login import check_login_state
from app.helpers.check_empty_file import check_file
from app.helpers.select_images import select_images

os.environ['TWITTER_SECRET_JSON'] = './Post_It/app/plataforms/twitter/Secrets/twitter_login.json' 

app = Flask(__name__,
            static_folder="app/web_interface/static",
            template_folder="app/web_interface/templates")

def create_app():
    @app.route('/')
    def home():
        return render_template('index.html')
    return app

@app.route('/', methods=['POST'])
def process_form():
    print(request.method)
    global redirect_url, redirect_user, handles
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

from app.plataforms.twitter.login_twitter import login_twitter_final
app.register_blueprint(login_twitter_final)

def Button_handler():
    global twitter, facebook, instagram, telegram, furaffinity, redirect_user, handles

    match request.form.get('submit_toggle'):
        case 'twitter_toggle':
            twitter = not twitter
            print(f'Twitter state {twitter}')
            handles['twitter_toggle'] = twitter
        case 'instagram_toggle':
            instagram = not instagram
            print(f'instagram state {instagram}')
            handles['instagram_toggle'] = instagram
        case 'facebook_toggle':
            facebook = not facebook
            print(f'facebook state {facebook}')
            handles['facebook_toggle'] = facebook
        case 'furaffinity_toggle':
            furaffinity = not furaffinity
            print(f'furaffinity state {furaffinity}')
            handles['furaffinity_toggle'] = furaffinity
        case 'telegram_toggle':
            telegram = not telegram
            print(f'telegram state {telegram}')
            handles['telegram_toggle'] = telegram

    match request.form.get('submit_login'):
        case 'twitter_login':
            if (twitter):
                global redirect_url, oauth1_twitter
                tuple = TL.handle_user()
                redirect_url = tuple[0]
                oauth1_twitter = tuple[1]
                redirect_user = True
                return  
        case 'instagram_toggle':
            pass
        case 'facebook_toggle':
            pass
        case 'furaffinity_toggle':
            pass
        case 'telegram_toggle':
            pass

    if request.form.get('select_image') == 'select_image':
        images = select_images()
        try:
            if os.path.isfile('./Post_It/app/temp/images.json'):
                os.remove('./Post_It/app/temp/images.json')
            with open('./Post_It/app/temp/images.json', 'w') as fp:
                print(images)
                json.dump(images, fp)
            fp.close()
        except:
            print('Deu não')

    if request.form.get('post') == 'post':
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
            os.remove('./temp/images.json')       
        except:
            print('File already deleted')

def init():
    global twitter, instagram, facebook, furaffinity, telegram, redirect_user, redirect_url, handles 
    handles = {
        'twitter_toggle': False,
        'instagram_toggle': False,
        'facebook_toggle': False,
        'furaffinity_toggle': False,
        'telegram_toggle': False
    }

    twitter, instagram, facebook, furaffinity, telegram = False, False, False, False, False
    redirect_user = False
    redirect_url  = None

try:
    with open(os.getenv('TWITTER_SECRET_JSON'), 'x+') as fp:
        print('Created tt_secrets File')
    fp.close()
except:
    print('Failed to create tt_secrets file')

try:
    os.makedirs('./Post_It/app/temp')
except:
    print('temp already exists')

try:
    os.makedirs('./Post_It/Secrets')
except:
    print('secrets already exists')

if os.path.isfile('./Post_It/app/temp/images.json'):
    os.remove('./Post_It/app/temp/images.json')

init()
create_app() 
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
