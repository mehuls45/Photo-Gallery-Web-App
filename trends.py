import tweepy
import re,os

os.chdir('C://xampp//htdocs//A')
file = open('Trends.csv', 'w')
 
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""
 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#trends = api.trends_place(2295420) # woeid code for India
trends = api.trends_place(1)
#trends = api.trends_place(23424975) # UK

for i in range(30):
    try:
        trend = trends[0]['trends'][i]['name']
        volume = str(trends[0]['trends'][i]['tweet_volume'])
        if volume == 'None':
            continue
        print(trend+','+volume)
        file.write(trend+','+volume)
        file.write('\n')
    except UnicodeEncodeError:
        flag = 1 # does nothing. Insignificant
