import os
from colorama import Fore, Style

def make_dirs():
    try:
        os.makedirs('./Post_It/Secrets')
        print(Fore.GREEN + '[STARTUP](project-folders): Created ./Post-It/Secrets folder')
    except:
        print(Fore.BLUE + '[STARTUP](project-folders): ./Post-It/Secrets already exists')

    try:
        os.makedirs('./Post_It/app/temp')
        print(Fore.GREEN + '[STARTUP](project-folders): Created ./Post-It/app/temp folder')
    except:
        print(Fore.BLUE + '[STARTUP](project-folders): ./Post-It/app/temp already exists')

    try:
        os.makedirs('./Post_It/app/plataforms/twitter/Secrets')
        print(Fore.GREEN + '[STARTUP](plataform-folders): Created .../plataforms/twitter/Secrets folder')
    except:
        print(Fore.BLUE + '[STARTUP](plataform-folders): .../plataforms/twitter/Secrets already exists')

def operate_files():
    if os.path.isfile('./Post_It/app/temp/images.json'):
        os.remove('./Post_It/app/temp/images.json') 
        print(Fore.RED + '[STARTUP](project-files): Removed ./Post-It/app/temp/images.json')

    try:
        with open(os.getenv('TWITTER_SECRET_JSON'), 'x+') as fp:
            print(Fore.GREEN + '[STARTUP](plataform-files): Created .../plataforms/twitter/Secrets/twitter_login.json')
        fp.close()
    except:
        print(Fore.RED + '[STARTUP](plataform-files): Failed to create .../plataforms/twitter/Secrets/twitter_login.json')
        print(Fore.RED + '|-------> It probably already exists')

def startup():
    make_dirs()
    operate_files()
    print(Fore.CYAN + '[STARTUP]: Startup phase finished' + Style.RESET_ALL)