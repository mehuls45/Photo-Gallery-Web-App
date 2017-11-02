import tweepy
import re,os

os.chdir('C://xampp//htdocs//A')
file = open('Trends.csv', 'w')
 
consumerKey = "1mH1dGHI5OHQZFJEYRncFSWNP"
consumerSecret = "GZEu1pR6UvSuuW2sO6JyBaegbTPPkeXMGiEFfZNLqVuUaL70le"
accessToken = "3104899826-IsgnoKKElfaJbEIhtUZ8hPbfmuUAsu0A35XP5EW"
accessTokenSecret = "05N6fDHfWecIdXj8DRrEsGT1fHzr9o1b0lA7W96gs5ALs"
 
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#trends = api.trends_place(2295420) # woeid code for India
trends = api.trends_place(1)
#trends = api.trends_place(23424975) # UK


#print(trends)

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
        flag = 1
        #print("")
    
#file.close() 
