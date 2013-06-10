#!/usr/bin/python 

from integration.adaptive import Adaptive

from domain.models import DataStore

def main():
  adaptive = Adaptive()
  tweet_items = adaptive.fetch_data()

  ds = DataStore()

  if tweet_items:
    for t in tweet_items:
      ds.insert_tweet(t)
  else:
    print "no results from adaptive api"

  for t in ds.get_all_tweets():
      print t

if __name__ == '__main__':
  main()