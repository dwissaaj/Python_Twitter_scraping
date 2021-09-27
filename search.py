import tweepy
import pandas as pd

auth =  tweepy.OAuthHandler("kKnqrEWzbC7ygcscbNYHTQIO6","OEN3Q49NNKAg5HcQbwCJ6PwJUjxgbQwmhqdGWTtYzn8uQq2PTQ")
auth.set_access_token("2209890762-KUmWTpz0hCZX1HHnYx8935H0s4JZzWAn8CcuDdT","fUKZMFbgWVafFtZiyRXCtCYIHJRucvAJHsAfa8VsBLrSW")
api = tweepy.API(auth)


number_of_tweet = 200
author = []
contributors = []
coordinates = []
date = []
entities = []
favorite = []
likes = []
favorited = []
tweets = []
geo = []
id = []
in_reply_to_screen_name = []
in_reply_to_status_id = []
in_reply_to_user_id = []
lang = []
parse = []
place = []
retweet = []
retweet_count = []
retweeted = []
retweeted_status = []
retweets = []
source = []
source_url = []
user = []


for i in tweepy.Cursor(api.search,q="kurir pos",tweet_mode="extended").items(number_of_tweet):
    author.append(i.author)
    contributors.append(i.contributors)
    coordinates.append(i.coordinates)
    date.append(i.created_at)
    entities.append(i.entities)
    favorite.append(i.favorite)
    likes.append(i.favorite_count)
    favorited.append(i.favorited)
    tweets.append(i.full_text)
    geo.append(i.geo)
    id.append(i.id)
    in_reply_to_screen_name.append(i.in_reply_to_screen_name)
    in_reply_to_status_id.append(i.in_reply_to_status_id)
    in_reply_to_user_id.append(i.in_reply_to_user_id)
    lang.append(i.lang)
    parse.append(i.parse)
    place.append(i.place)
    retweet.append(i.retweet)
    retweet_count.append(i.retweet_count)
    retweeted.append(i.retweeted)
    retweets.append(i.retweets)
    source.append(i.source)
    source_url.append(i.source_url)
    user.append(i.user.screen_name)

df = pd.DataFrame({'author':author,'contributor': contributors,'coordinates': coordinates,'date':date,
                   "entities": entities,'favorite':favorite,'likes':likes,'tweet':tweets,
                   "geo":geo,'id':id,'in_reply_to_screen_name':in_reply_to_screen_name,'in_reply_to_status_id':in_reply_to_status_id,
                   'in_reply_to_user_id':in_reply_to_user_id,'lang':lang,'parse':parse,'place':place,'retweet':retweet,'retweet_count':retweet_count,
                   'retweeted':retweeted,'retweets':retweets,'source':source,'source_url':source_url,'user':user})

#menghilangkan RT
#df= df[~df.tweets.str.contains("RT")]

import openpyxl


