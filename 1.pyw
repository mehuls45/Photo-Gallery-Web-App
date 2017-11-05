#! python3

from tweepy import Stream
from tweepy import OAuthHandler                       # Oauth is authentication handler
from tweepy.streaming import StreamListener  # listens to twitterd data stream
import os,time,re
import subprocess

os.chdir('C://xampp//htdocs//A') # change directory
LinkList = [] # list of links for which images are to be downloaded, distinct and unique
Search = ''

#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""

class listener(StreamListener):

    def on_data(self, data):
        try:
            # data contains all the details that the tweepy API returns
            tweet = data.split(',"media_url":"http:')[1].split('","')[0]   # split and search in data.. to receive image links

            tweet = re.sub('\\\/','/',tweet)    # substiute in link, so that the images are downloadable from link
            newTweet = 'http:' + tweet  # add hyper text to link

            if len(LinkList)>=9:  # checks that only 9 links are extracted
                os._exit(0)  # exit if 9 links found

            if newTweet not in LinkList:   # if the given link, is distinct store it... else, ignore
                LinkList.append(newTweet)
                print(newTweet)    # and print it

                saveFile = open('ImageLinks.csv','a')  # open Link folder
                saveFile.write(newTweet) # Write link in CSV
                saveFile.write('\n') # end line
                saveFile.close() close file
                return(True) # successfully written..
            
        except BaseException:  # if image link not found, failed on data
            print('failed ondata')

    def on_error(self, status): # dont know
        print(status)


if os.path.exists('ImageLinks.csv'):    # if old link folder exists...
    os.remove('ImageLinks.csv')                     # remove it
        
auth = OAuthHandler(ckey, csecret)   # Setting the authenticating parameters
auth.set_access_token(atoken, asecret)   # Set access token so that, stream can be listened...

fr = open('getKey.txt','r')   # open the file where keyword is written
Search = fr.read()  # read the keyword from file
    
twitterStream = Stream(auth, listener())  # Pass authentication parameters to, listen to stream
twitterStream.filter(track=[Search]) # Passes the given keyword and searches for it in the stream..

