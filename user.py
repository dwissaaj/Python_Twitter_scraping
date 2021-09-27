import tweepy
import pandas as pd

auth =  tweepy.OAuthHandler("kKnqrEWzbC7ygcscbNYHTQIO6","OEN3Q49NNKAg5HcQbwCJ6PwJUjxgbQwmhqdGWTtYzn8uQq2PTQ")
auth.set_access_token("2209890762-KUmWTpz0hCZX1HHnYx8935H0s4JZzWAn8CcuDdT","fUKZMFbgWVafFtZiyRXCtCYIHJRucvAJHsAfa8VsBLrSW")
api = tweepy.API(auth)

pos_tweet = api.user_timeline(id="posindonesia",count=200,page=1)
"""for tweet in pos_tweet:
    print(tweet.user.screen_name)"""


