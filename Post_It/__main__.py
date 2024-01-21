import Twitter.twitter as TT
import Twitter.login_twitter as TL

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