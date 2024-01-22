import json, os

def check_login_state() -> bool:
    check_file = os.stat('./Post_It/app/Twitter/Secrets/twitter_credentials.json').st_size

    if(check_file == 0):
        print("The file is empty.")
    else:
        print("The file is not empty.")
        with open('./Post_It/app/Twitter/Secrets/twitter_credentials.json', 'r') as fp:
            twitter_credentials = json.load(fp)

    try: 
        if twitter_credentials['ACCESS_TOKEN'] == None or twitter_credentials['ACCESS_SECRET'] == None:
            raise UnboundLocalError 
        else:
            print('Logged in')   
            return True
    except:
        print('Not logged in')
        return False
        #TODO: Warn user in the GUI hes not logged in yet
        #TODO: Implement not logged in message