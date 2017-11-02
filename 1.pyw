#! python3

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os,time,re
import subprocess

os.chdir('C://xampp//htdocs//A')
LinkList = []
Search = ''

#consumer key, consumer secret, access token, access secret.
ckey="1mH1dGHI5OHQZFJEYRncFSWNP"
csecret="GZEu1pR6UvSuuW2sO6JyBaegbTPPkeXMGiEFfZNLqVuUaL70le"
atoken="3104899826-IsgnoKKElfaJbEIhtUZ8hPbfmuUAsu0A35XP5EW"
asecret="05N6fDHfWecIdXj8DRrEsGT1fHzr9o1b0lA7W96gs5ALs"

class listener(StreamListener):

    def on_data(self, data):
        try:
            # data contains all the details that the tweepy API returns
            tweet = data.split(',"media_url":"http:')[1].split('","')[0]

            tweet = re.sub('\\\/','/',tweet)
            newTweet = 'http:' + tweet

            if len(LinkList)>=9:
                os._exit(0)

            if newTweet not in LinkList:
                LinkList.append(newTweet)
                print(newTweet)

                saveFile = open('ImageLinks.csv','a')
                saveFile.write(newTweet)
                saveFile.write('\n')
                saveFile.close()
                return(True)
            
        except BaseException:
            print('failed ondata')

    def on_error(self, status):
        print(status)


if os.path.exists('ImageLinks.csv'):
    os.remove('ImageLinks.csv')

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

fr = open('getKey.txt','r')
Search = fr.read()
    
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[Search]) # Replace the search word here

