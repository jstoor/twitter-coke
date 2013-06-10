#!/usr/bin/python 

from flask import Flask, render_template
from integration.adaptive import Adaptive
from domain.models import DataStore

app = Flask(__name__)

@app.route('/')
def index():
    """
    Each time called, retieve the latest set of data from the adaptive api.
    If data returned, store the new data and then fetch all tweets, before rendeering the results.
    """
    adaptive = Adaptive()
    tweet_items = adaptive.fetch_data()
    
    if tweet_items:
      with DataStore() as ds:
        ds.insert_tweets(tweet_items)

        tweet_list = ds.get_all_tweets()

      result = render_template('index.html', tweet_list=tweet_list, error_message='')
    else:
      result = render_template('index.html', tweet_list=[], error_message='No Results, Folks!')

    return result


if __name__ == "__main__":
    app.run(port=7000)