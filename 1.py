#! python3

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os,time,re

os.chdir('C://Users//Mehul//Desktop//Pin')
LinkList = []

#consumer key, consumer secret, access token, access secret.
ckey=" "
csecret=" "
atoken=" "
asecret=" "

class listener(StreamListener):

    def on_data(self, data):
        try:
            #print(data)

            tweet = data.split(',"media_url":"http:')[1].split('","')[0]
            #print(str(tweet))

            #print(tweet)

            tweet = re.sub('\\\/','/',tweet)
            newTweet = 'http:' + tweet

            if newTweet not in LinkList:
                LinkList.append(newTweet)
                print(newTweet)

            if len(LinkList)>=10:
                exit()

            saveFile = open('ImageLinks.csv','a')
            saveFile.write(newTweet)
            saveFile.write('\n')
            saveFile.close()
            return(True)
        except BaseException:
            print('failed ondata')
            #time.sleep(5)

    def on_error(self, status):
        print(status)


if os.path.exists('ImageLinks.csv'):
    os.remove('ImageLinks.csv')

    
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ball"]) # Replace the search word here
