import time
import pymongo
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

HOST = 'mypg'
PORT = '5432' #port inside the container
DATABASE = 'postgres'
USER = 'postgres'
PASSWORD = 'postgres'

#define functions:
def extract():
    ''' reads data from MongoDB and return the tweets in a dataframe'''
    db = client.mymongo_db #or should it be client.mymongo_db?
    tweets = db.my_tweets.find()
    df = pd.DataFrame(tweets) #convert entire collection to Pandas dataframe
    return df

def transform(df):
    df['text']=df['text'].apply(clean_tweets)
    analyser = SentimentIntensityAnalyzer()
    pol_scores = df['text'].apply(analyser.polarity_scores).apply(pd.Series)
    df=pd.concat([df, pol_scores['compound']], axis=1)
    return df


def load(df):
    # store the result in the a postgres database
    df.to_sql('tweets', pg, if_exists='replace')

def clean_tweets(tweet):
    mentions_regex= '@[A-Za-z0-9]+'  # "+" means one or more times
    url_regex='https?:\/\/\S+' # this will catch most URLs; "?" means 0 or 1 time; "S" is anything but whitespace
    hashtag_regex= '#'
    rt_regex= 'RT\s'
    tweet = re.sub(mentions_regex, '', tweet)  # removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) # removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) # removes RT to announce retweet   
    tweet = re.sub(url_regex, '', tweet) # removes most URLs
    tweet = re.sub(':', '', tweet)
    return tweet

time.sleep(20)

#connect to mongo
client = pymongo.MongoClient(host='mongodb', port=27017)

# Connect to Postgres
pg = create_engine(f'postgresql://postgres:postgres@{HOST}:5432/{DATABASE}', echo=True)
pg.execute('drop table if exists tweets;')
pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

while True:
   load(transform(extract()))  
   time.sleep(20) 

