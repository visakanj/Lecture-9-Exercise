from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk

## SI 507 - HW
## COMMENT WITH:
## Your section day/time: Section 009, Monday 4-5:30pm
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username> <num_tweets>
username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
#requests.get(url, auth=auth)
#Code for OAuth ends

#Write your code below:
# Part 1: Fetch 25 tweets from UMSI account
baseurl = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params_dict = {"screen_name": "@" + username, "count": num_tweets}
response = requests.get(baseurl, params_dict, auth = auth)
twitter_results = response.text
twitter_results_json = json.loads(response.text)

#print(twitter_results_json)
#dumped_json = json.dumps(twitter_results)

#JSON_FILE = "tweet.json"

#json_file = open(JSON_FILE, "w")
#json_file.write(dumped_json)
#json_file.close()

for tweet in twitter_results_json:
	print("\n")
	print(tweet["user"]["name"], ":")
	print(tweet["text"])




