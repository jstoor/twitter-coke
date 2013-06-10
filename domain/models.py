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

  def close(self):
    self.session.connection().close()

  def insert_tweet(self, tweet):
    # Check if the tweet already exists.
    #if self.session.query(Tweet).filter_by(id=tweet.id).count() == 0:
      self.session.add(tweet)
      self.session.commit()
    #else:
      # TODO : Update the record ???
      #pass

  def get_all_tweets(self):
    #stmt = select(['tweet.id', 'tweet.tweet_id', func.count('tweet.tweet_id'), from_obj=['tweet']])
             #group_by(tweet_id)

    #return self.session.execute(stmt).fetchall()  

    result = self.session.query(Tweet.id, Tweet.tweet_id,
        func.count(Tweet.tweet_id), Tweet.message, Tweet.followers, Tweet.user_handle, Tweet.sentiment).group_by(Tweet.tweet_id).order_by('sentiment').all()

    

    #result = self.session.query(Tweet).group_by('tweet_id').columns(Tweet.type,  func.count('*')).execute().fetchall() 


    #tweet_items = self.session.query(Tweet).group_by('tweet_id').order_by('sentiment').all()
    #for t in tweet_items:
    #  print t
    #return tweet_items
    #print "---------------------------------------"

    #data = self.session.execute('select * from tweet', mapper=Tweet)
    #for i in data:
    #  print i
    #print "---------------------------------------"
    return result









