from urllib import response
import requests, json 


# Joke API

captionURL = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas"

try:

  response = requests.get(captionURL)
  res = json.loads(response.text)
  res = res["setup"]+" "+res["delivery"]

except:
  
  print("Error While calling API")