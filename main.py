#!/usr/bin/python 

from integration.adaptive import Adaptive

from domain.models import DataStore

def main():
  adaptive = Adaptive()
  tweet_items = adaptive.fetch_data()

  with DataStore() as ds:

    if tweet_items:
      ds.insert_tweets(tweet_items)
    else:
      print "no results from adaptive api"

    all_tweets = ds.get_all_tweets()

    for t in all_tweets:
        print t

if __name__ == '__main__':
  main()