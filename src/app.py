
import requests
import tweepy
import pandas as pd
import re
import seaborn as sns
import matplotlib as plt
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    

import os 

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

print(consumer_key)
print(consumer_secret)
print(bearer_token)

# Creando cliente de Twitter
client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

# Definiendo la query para Twitter

query = '#100daysofcode (pandas OR python) -is:retweet'     

tweets = client.search_recent_tweets(query=query, 
                                    tweet_fields=['author_id','created_at','lang'],
                                     max_results=100)

tweets
