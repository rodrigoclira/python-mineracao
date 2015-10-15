#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "18857274-dZHV342QWSXm0MYFVmUwRbnMywu3XUJJArPvqeYS4"
access_token_secret = "a4NRP2rFRpExr6BH0AworloLn65to4eUJh8niUsGGu5JP"
consumer_key = "22p11D7m5te9ifHa6ESQD6ZEi"
consumer_secret = "Q6o0YXCK7Pi7AzcWlKY26FwVfUkayViG0KkRkQfsg79KiptTkD"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
