import tweepy
import csv
import re

apikeyData = open("apikey", "r").read().split(',')
consumer_key = apikeyData[0]
consumer_secret = apikeyData[1]
access_token = apikeyData[2]
access_token_secret = apikeyData[3]

tweets_for_csv = []

def get_hashtag(hashtag):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    limit = 5
    print('- Hashtag : '+hashtag)

    for tweet in tweepy.Cursor(api.search, q=hashtag+'-filter:retweets', tweet_mode="extended").items(limit):
        actualTweet = re.sub(r'\s+', ' ', tweet.full_text)
        tweets_for_csv.append(
            [hashtag, tweet.created_at, tweet.id, actualTweet])

if __name__ == '__main__':
    tags = ['#gempa', '#kebakaran', '#banjir', '#tsunami']

    print("\nGet tweet from hashtag ...")
    for tag in tags:
        get_hashtag(tag)

    outfile = "search-hashtag.csv"
    with open(outfile, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["hashtag", "datetime", "tweet_id", "tweet"])
        csvwriter.writerows(tweets_for_csv)
    
    print("\nwriting to '" + outfile + "' complete.")