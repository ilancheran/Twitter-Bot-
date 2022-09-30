import tweepy
from randomCats import *


api_key = "WSyG8byy7PYl1PC3A1OB15uRw"
api_key_secret = "IRRV25deTgDbvuGxXELInvc7oKW8jg0cFYDsF4ONsNFNiMxB95"
api_access_token = "1575366145099833345-yqCSI5wR5N9kKlgJp81Z7IpGl5nw1v"
api_access_token_secret = "yTfKZnsgAkcUxryh5tZqH8OiT2ISdj4qb2VsLN2RdpJPZ"


try:
  auth = tweepy.OAuthHandler(api_key,api_key_secret)
  auth.set_access_token(api_access_token, api_access_token_secret)
except:
  print("Authentication Error")


def post():

  api = tweepy.API(auth)
  api.verify_credentials()

  text =  res 
  new_tweet ="local-filename.jpg"
  api.update_status_with_media(text,new_tweet)