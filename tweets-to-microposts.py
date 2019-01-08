import csv
from datetime import datetime

OUTPUT_PATH = "output/microposts/"

def write_micropost(tweet_datetime, tweet_content):
    filename = tweet_datetime.strftime("%Y-%m-%dT%H%M") + ".md"
    fout = open(OUTPUT_PATH + filename, 'w')
    fout.write('---\n')
    fout.write('title: "' + tweet_datetime.isoformat() + '"\n')
    fout.write('date: "' + tweet_datetime.isoformat() + '"\n')
    fout.write('---\n')
    fout.write('\n')
    fout.write(tweet_content + "\n")
    fout.close()

def create_new_micropost(tweet):
    tweet_datetime = datetime.strptime(tweet["timestamp"], "%Y-%m-%d %H:%M:%S %z")
    tweet_content = tweet["text"] + " " + tweet["expanded_urls"]
    write_micropost(tweet_datetime, tweet_content)

with open('data/tweets.csv') as csvfile:
    tweetsreader = csv.DictReader(csvfile, delimiter=',')
    for tweet in tweetsreader:
        create_new_micropost(tweet)
