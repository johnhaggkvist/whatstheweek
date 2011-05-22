import twitter
import time

class Tweeter:
    api = None
    def __init__(self):
        self.api = twitter.Api(
            consumer_key='x',        # need
            consumer_secret='x',     # to
            access_token_key='x',    # change
            access_token_secret='x') # this ;)

    def hasTweeted(self, txt):
        statuses = self.api.GetUserTimeline('whatstheweek')
        for status in statuses:
            if (status.text == txt):
                return True
        return False

    def tweet(self, txt):
        status = self.api.PostUpdate(txt)
        return status.text

def main():
    week = time.strftime("%W")
    tweeter = Tweeter()
    if not tweeter.hasTweeted(week):
        status = tweeter.tweet(week)
        print "Tweeted "+status
    else:
        print "Already tweeted "+str(week)

main()