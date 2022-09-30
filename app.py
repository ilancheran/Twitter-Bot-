from email.mime import application
from flask import Flask
import twitterbot
import schedule 
import time

application = Flask(__name__)

@application.route("/")

def job():
  twitterbot.post()
  print("success")

schedule.every().day.at("10:00").do(job)
schedule.every().day.at("14:00").do(job)


while True :
  schedule.run_pending()
  time.sleep(60)


