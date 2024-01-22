def check_login_state(AT: str, AS: str):
    try: 
        if AT == None or AS == None:
            raise UnboundLocalError 
        else:
            print('Logged in')   
    except:
        print('Not logged in')
        #TODO: Warn user in the GUI hes not logged in yet
        #TODO: Implement not logged in message