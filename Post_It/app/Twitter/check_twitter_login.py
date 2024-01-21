def check_login_state(AT: str, AS: str):
    try: 
        if AT == None or AS == None:
            raise UnboundLocalError    
    except:
        print('Not logged in')
        exit()
        #TODO: Warn user in the GUI hes not logged in yet
        #TODO: Implement not logged in message