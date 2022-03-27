import pandas as pd
import textblob
import re
import matplotlib.pyplot as plt

df = pd.read_csv("read_data.csv", encoding="latin1")

# clean data
# create a function
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # simply removes @ mentions
    text = re.sub(r'#', '', text)  # removes the # symbol
    text = re.sub(r'RT[\s]+', '', text)  # removes the retweets(RT)
    text = re.sub(r'https?:\/\/\S+', "", text)  # remove the hyperlink
    return text


# cleaning text from database of tweets
df["Tweet"] = df["Tweet"].apply(cleanTxt)

# Create a function to get the subjectivity
def getSubjectivity(text):
    return textblob.TextBlob(text).sentiment.subjectivity


# Creating a function to get polarity of tweets
def get_polarity(text):
    return textblob.TextBlob(text).sentiment.polarity


# creating two new columns for subjectivity and polarity
df["subjectivity"] = df['Tweet'].apply(getSubjectivity)
df["polarity"] = df['Tweet'].apply(get_polarity)


# create a function to compute the negative, neutral and positive
def get_analysis(score):
    if score < 0:
        return "negative"
    elif score > 0:
        return "positive"
    else:
        return "neutral"


def get_trade_analysis(score):
    if score < 0:
        return "SELL"
    elif score > 0:
        return "BUY"
    else:
        return "HOLD"


df["Analysis"] = df["polarity"].apply(get_analysis)
df["Stock Trade Analysis"] = df["polarity"].apply(get_trade_analysis)


# plotting the analysis in bar graph form
df["Analysis"].value_counts()
plt.title("Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Counts")
df["Stock Trade Analysis"].value_counts().plot(kind="bar")
plt.show()
df.to_csv("analysed_data.csv")