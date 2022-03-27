import tweepy
import configparser
import pandas as pd

# reading API information from config file
config = configparser.ConfigParser()
config.read('/config.ini')
api_key = config["TWITTER"]["api_key"]
api_key_secret = config["TWITTER"]["api_key_secret"]
access_token = config["TWITTER"]["access_token"]
access_token_secret = config["TWITTER"]["access_token_secret"]

# authorization using tweepy
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = "elonmusk"
user_info = api.get_user(screen_name=user)
name = user_info.name

elon_tweets = api.user_timeline(screen_name='elonmusk', count=100, include_rts=False, tweet_mode='extended')
# generating data of elon musk tweets
columns = ["Tweet", "Time", "User"]
data = []
for tweet in elon_tweets[:]:
    data.append([tweet.full_text, tweet.created_at, "elonmusk"])
df = pd.DataFrame(data, columns=columns)
df.to_csv("read_data.csv")
