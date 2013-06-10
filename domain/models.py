#!/usr/bin/python 

from sqlalchemy import Column, Integer, String,  engine, create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import select, func

BASE = declarative_base()

class Tweet(BASE):
  __tablename__ = "tweet"

  id = Column(Integer, Sequence('id', start=1, increment=1),primary_key=True)
  tweet_id = Column(Integer)
  user_handle = Column(String)
  message = Column(String)
  followers = Column(Integer)
  sentiment = Column(Integer)

  def __init__(self, tweet_id, user_handle, message, followers, sentiment):
    self.tweet_id = tweet_id
    self.user_handle = user_handle
    self.message = message
    self.followers = followers
    self.sentiment = sentiment

  def __repr__(self):
    return "<Tweet('%d', '%d', %s', '%s', '%s', '%s')>" % (self.id, self.tweet_id, self.user_handle, self.message, self.followers, self.sentiment)


class DataStore(object):
  def __init__(self):
    engine = create_engine("sqlite:///tweet.db", echo=False)
     
    metadata = BASE.metadata
    metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    self.session = Session()

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self.session.connection().close()

  def insert_tweet(self, tweet):
    self.session.add(tweet)
    self.session.commit()

  def insert_tweets(self, tweets):
    for tweet in tweets:
      self.insert_tweet(tweet)

  def get_all_tweets(self):
    raw_list = self.session.query(Tweet.id, Tweet.tweet_id,
        func.count(Tweet.tweet_id), Tweet.message, Tweet.followers, Tweet.user_handle, Tweet.sentiment).group_by(Tweet.tweet_id).order_by('sentiment desc').all()

    result = []

    # raw_list is a tuple, so we need to convert to a dictioanry so that calling code can refer to attributes, rather than indexes.
    # NOTE : Investigate better/cleaner way to resolve this.
    result = [dict(zip(['id','tweet_id', 'count','message','followers','user_handle','sentiment'],item)) for item in raw_list]

    return result









