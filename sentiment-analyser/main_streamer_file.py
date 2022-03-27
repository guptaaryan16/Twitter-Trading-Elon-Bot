import json
import tweepy
import configparser
import re
import textblob
import csv


# first we are going to create the trade analyser as stream works according to that
# building a NLP sentiment analyser first so that we can really understand the tweets' contents
def cleanTxt(text):
    text = re.sub(r",", "", text)  # remove commas s that we can easily write to csv files
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # simply removes @ mentions
    text = re.sub(r'#', '', text)  # removes the # symbol
    text = re.sub(r'RT[\s]+', '', text)  # removes the retweets(RT)
    text = re.sub(r'https?:\/\/\S+', "", text)  # remove the hyperlink
    return text


# Create a function to get the subjectivity
def getSubjectivity(text):
    return textblob.TextBlob(text).sentiment.subjectivity


# Creating a function to get polarity of tweets
def get_polarity(text):
    return textblob.TextBlob(text).sentiment.polarity


def get_stock_trade_analysis(text):
    text = cleanTxt(text)
    polarity_score = get_polarity(text)
    if polarity_score < 0:
        return "SELL"
    elif polarity_score > 0:
        return "BUY"
    else:
        return "HOLD"


# sample function to demonstrate what the finance api would do if we deploy it using this information
def make_trades(trade_analysis):
    if trade_analysis == "SELL":
        # Now here we will deploy a trading model that will take these as input
        print("SELL")
    elif trade_analysis == "BUY":
        print("BUY")
    else:
        print("HOLD")


# Now we are going to make the livestreaming part of the code. This will provide us the information about the trades.
# reading API information from config file
config = configparser.ConfigParser()
config.read("config.ini")
# if configparser does not work just create usual entries with configparser part removed.
api_key = config["TWITTER"]["api_key"]
api_key_secret = config["TWITTER"]["api_key_secret"]
access_token = config["TWITTER"]["access_token"]
access_token_secret = config["TWITTER"]["access_token_secret"]

# authorization using tweepy
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
columns = ["Tweet", "Time", "User"]
tweets = []

# Now we are going to make a csv file that will hold all the trades made
f = open('trade_data.csv', 'w')
writer = csv.writer(f)

class IDPrinter(tweepy.Stream):

    def on_data(self, rawdata):
        tweet = json.loads(rawdata)
        if tweet["user"]["screen_name"] == "elonmusk":
            analysis = get_stock_trade_analysis(tweet["text"])
            text = cleanTxt(tweet["text"])
            make_trades(analysis)
            writer.writerow(
                [cleanTxt(tweet["text"]), tweet["created_at"], "elonmusk", getSubjectivity(text), get_polarity(text),
                 analysis])


printer = IDPrinter(
    api_key, api_key_secret,
    access_token, access_token_secret
)


# Initialize instance of the subclass
def start_trading(LiveStream=False):  # you can make it set to True if you want livestream
    if LiveStream:
        printer.filter(track=["Tesla", "SpaceX", "Dogecoin", "elonmusk"])


start_trading(LiveStream=True)
