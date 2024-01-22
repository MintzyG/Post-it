import json, os
from ..helper_functions.check_empty_file import check_file

path = os.getenv('TWITTER_SECRET_JSON')
def check_login_state() -> bool:
    file_state = check_file(path)

    if (file_state):
        with open(path, 'r') as fp:
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