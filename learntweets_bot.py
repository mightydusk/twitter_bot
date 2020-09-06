import tweepy
import os
def create_api():
  consumer_key=os.getenv('consumer_key')
  consumer_secret=os.getenv('consumer_secret')
  access_token=os.getenv('access_token')
  access_token_secret=os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print("API Created")
  return api
import time
def emonum(user):
  emo_num={0:"0️⃣",1:"1️⃣",2:"2️⃣",3:"3️⃣",4:"4️⃣",5:"5️⃣",6:"6️⃣",7:"7️⃣",8:"8️⃣",9:"9️⃣"}
  u_split=[int(i) for i in str(user.followers_count)]
  u_emo=''.join([emo_num[j] for j in u_split if j in emo_num.keys()])
  return u_emo

api = create_api()
while True:
  user=api.get_user('learntweetsapi')
  api.update_profile(name =f'learntweet{emonum(user)}')
  print(f'Updating Name : learntweet|{emonum(user)}')
  print('WAITING TO REFRESH')
  time.sleep(60)
     
