# Elon Musk Twitter Trading Bot
This is a flask based web application designed to show the sentiment analysis done for tweets and to display them on the website. Ths project uses Textblob and pandas to make an effective analysis of the data and to provide enough information about the details. I am also trying to integrate it with a stock trading API to make effective trades with this data.
# Requirements
- flask
- pandas
- json
- tweepy(v4.8.0)
- configparser
- re
- textblob
- csv
- configparser
# Usage
- For using this you need to generate a twitter developer account request through https://developer.twitter.com and then generate a new API project. Then you will get access to API keys and TOKEN keys. Now you need to enter this information in the congig.ini file present in the sentiment-analyser directory.
- Once that is done you just need to run sentiment_analysis.py and all the information will get stored in trade_data.csv file.
- Now you can see the information available on the Flask website by running app.py file (possibly on another IDE).
# About the project
This project involves taking data from twitter using Tweepy library from python and then analysing it from TextBlob library and then making analysis of whether to buy, sell or hold the stock. This project is made as part of the MAKERS assignment of SDSLabs, a campus group at IIT Roorkee.
Through this project I gained knowledge in a lot of aspects about software engineering and algorithms in general as well as APIs and Machine Learning. I would like to thank SDSLabs for providing me the opportunity to work on this project and give my best to initial attempts at learning in open-source. I learned about pandas, sentiment analysis, flask and web development.
# Developer Details 
Aryan Gupta
(EE, IITR)
