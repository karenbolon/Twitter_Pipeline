import tweepy
import logging
import pymongo
#import time
import os

#from sqlalchemy import create_engine

# establish connection to client
# if only one client is running:
client = pymongo.MongoClient(host='mongodb', port=27017)

# define db 
db = client.mymongo_db # 'mymongo_db' is name of db

# define collection
dbtweets = db.my_tweets # 'my_db' is name of db

#bearer token for twitter
client_tweepy = tweepy.Client(
    bearer_token=os.getenv('BEARER_TOKEN'),
    wait_on_rate_limit=True,
)

#get twitter feeds
response = client_tweepy.get_user(
    username='GeorgeTakei',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url','verified']
)

user = response.data

#print(dict(user))

#create a for loop (supposed to stream live but I have limited it to 100)
num_results = 100
result_count = 0

while result_count <  num_results:    
    cursor = tweepy.Paginator(
        method=client_tweepy.get_users_tweets,
        id=user.id,
        exclude=['replies'],  #, 'retweets'
        tweet_fields=['author_id', 'created_at', 'public_metrics']
    ).flatten(limit=100)

    result_count += 1

#for tweet in cursor:
#    print(tweet.text)

search_query = "george takei -is:retweet -is:reply -is:quote lang:en -has:links"

cursor = tweepy.Paginator(
    method=client_tweepy.search_recent_tweets,
    query=search_query,
    tweet_fields=['author_id', 'created_at', 'public_metrics'],
).flatten(limit=100)

for tweet in cursor:
    print(tweet.text)
    logging.critical(f'{tweet.text}')
    mydict={'text':tweet.text}
    dbtweets.insert_one(mydict) 

# print twitter news
for my_doc in dbtweets.find():
  print(my_doc, end='\n\n') 

# in mongo shell you can see the tweets via: db.my_collection.find()

# when was the last tweet sent?
#my_doc['found_tweet']
#my_doc['found_tweet']['time']
