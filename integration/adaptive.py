#!/usr/bin/python 

from urllib2 import urlopen, HTTPError
from json import loads
from domain.models import Tweet

API_URL = "http://adaptive-test-api.herokuapp.com/tweets.json"

class Adaptive(object):
  def fetch_data(self):
    """ 
    Makes a call to the third-party api and returns the data or 
    None if an HTTPError occurred. 
    """ 
    try:
      raw_data = urlopen(API_URL).read()
      # Convert the returned string to a real list.
      tweet_items = loads(raw_data)
      
      result = []

      for item in tweet_items:
        result.append(Tweet(
          item['id'],
          item['user_handle'],
          item['message'],
          item['followers'],
          item['sentiment']
          ))

      return result

    except HTTPError, ex:
      # TODO : Perhaps log the errors, in case we want to monitor how often
      # the third party service fails. Occasionaly might be acceptable, but
      # too often, may be unacceptable.
      return None

