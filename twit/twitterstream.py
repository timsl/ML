import tweepy
from tweepy import OAuthHandler

consumer_key = 'hqNRydYbOVHppSpFjL1ROW2e3'
consumer_secret = 'CsDb2BpyESRmcpkLJyc3M5Z8lHalG1ZNqWMYMwZ19JvftKXaN9'
access_token = '483161308-xFEo2rmHlTWWm0SBTsmeOFH8ohydLKNl0IDT8QUB'
access_secret = 'STx3cplZCLyCfhnsCHXnRZRI8mZmqXRZHLZHGZHzJOB1L'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#google'])
