from PIL import Image
import requests, json 
import urllib.request
from randomJoke import *


catURL = 'http://aws.random.cat/meow'


try:
    
  imageURL = json.loads(requests.get(catURL).content)["file"]
  urllib.request.urlretrieve(imageURL, "local-filename.jpg")

except:

  print("Error While Calling API")


