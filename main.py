import tweepy
from gpt3 import gpt3_response
import time
import datetime
import pytz
from decouple import config


api_key = config('api_key',default='')
api_secrets = config('api_secrets',default='')
access_token = config('access_token',default='')
access_secret = config('access_secret',default='')
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

mention_id = 1

date_time = datetime.datetime.now()

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print("Mention Tweet Found!")
        print(f"{mention.author.screen_name} - {mention.text}")
        mention_id = mention.id
        question = " ".join(mention.text.split()[1:])
        response = gpt3_response(question)[1:]
        try :
            print("Replying...")
            status = f'@{mention.author.screen_name}' + response
            api.update_status(status=status, in_reply_to_status_id= mention.id_str)
            print('Success')
        except Exception:
            print(Exception)
    time.sleep(10)
