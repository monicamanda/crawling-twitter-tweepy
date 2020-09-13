import tweepy
import csv
import re

apikeyData = open("apikey", "r").read().split(',')
consumer_key = apikeyData[0]
consumer_secret = apikeyData[1]
access_token = apikeyData[2]
access_token_secret = apikeyData[3]

tweets_for_csv = []

def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    limit = 5
    print('- Username : @'+username)

    for tweet in tweepy.Cursor(api.user_timeline, screen_name=username, include_rts=False, tweet_mode='extended').items(limit):
        actualTweet = re.sub(r'\s+', ' ', tweet.full_text)
        tweets_for_csv.append(
            [username, tweet.created_at, tweet.id, actualTweet])

if __name__ == '__main__':
    users = ['infobmkg', 'bnpb_indonesia', 'petabencana', 'bencanaID']
    
    print("\nGet tweet from username ...")
    for user in users:
        get_tweets(user)

    outfile = "user-timeline.csv"
    with open(outfile, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["username", "datetime", "tweet_id", "tweet"])
        csvwriter.writerows(tweets_for_csv)
    
    print("\nwriting to '" + outfile + "' complete.")
