import tweepy  # twitter API
import re,os

os.chdir('C://xampp//htdocs//A')
file = open('Trends.csv', 'w')   # open treans file to write
 
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""
 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)  # set authentication parameter
auth.set_access_token(accessToken, accessTokenSecret) # set access token
api = tweepy.API(auth) # pass parameter and get authentication

#trends = api.trends_place(2295420) # woeid code for India
trends = api.trends_place(1) # woeid for world
#trends = api.trends_place(23424975) # UK

for i in range(30): # try 30 times
    try:
        trend = trends[0]['trends'][i]['name']                    # get trend name from json format JSON: Java Script object notation is the way how twitter API returns data
        volume = str(trends[0]['trends'][i]['tweet_volume'])      # get trend volume 
        if volume == 'None':  # if tweet does not have count, don't store.
            continue
        print(trend+','+volume) # else store and print
        file.write(trend+','+volume)
        file.write('\n')
    except UnicodeEncodeError:                         # check exception, so that does not fail on encouter with other languages
        flag = 1 # does nothing. Insignificant
