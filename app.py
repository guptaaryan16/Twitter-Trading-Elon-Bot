from flask import Flask, render_template, url_for, flash, redirect
import pandas as pd

app = Flask(__name__)

sample_data = pd.read_csv("sentiment-analyser/Tweet_reader_sample/analysed_data.csv", index_col=None)
trade_data = pd.read_csv("sentiment-analyser/trade_data.csv")

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/tweets_made")
def tweets_made():
    return render_template("tweets_made.html", tables=[sample_data.to_html()], titles=[''])

@app.route("/register")
def register():
    return render_template("register.html", tables=[trade_data.to_html()], titles=[''])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
