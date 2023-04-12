import pandas as pd
import tweepy
import datetime
from dotenv import load_dotenv
import os
load_dotenv()
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_key = os.environ.get('ACCESS_KEY')
access_secret = os.environ.get('ACCESS_SECRET')

def scrape(words, date_since, numtweet,api,key):
    db = pd.DataFrame(columns=['username',
                               'description',
                               'location',
                               'following',
                               'followers',
                               'totaltweets',
                               'retweetcount',
                               'text',
                               'hashtags'])

    # We are using .Cursor() to search
    tweets = tweepy.Cursor(api.search_tweets,
                           words, lang="en",
                           since_id=date_since,
                           tweet_mode='extended').items(numtweet)

    # .Cursor() returns an iterable object.
    list_tweets = [tweet for tweet in tweets]

    # Counter to maintain Tweet Count
    i = 1
    final_list = list()
    # we will iterate over each tweet in the
    for tweet in list_tweets:
        view_dict = dict()
        view_dict['username'] = tweet.user.screen_name
        view_dict['location'] = tweet.user.location
        view_dict['totaltweets'] = tweet.user.statuses_count
        view_dict['retweetcount'] = tweet.retweet_count

        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        # Retweets can be distinguished by a retweeted_status attribute
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])


        view_dict['description'] = text
        view_dict['hashtags'] = hashtext
        final_list.append(view_dict)

        # Here we are appending all the
        ith_tweet = [username, description,
                     location, following,
                     followers, totaltweets,
                     retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
        i = i + 1
    filename = os.getcwd()+'/base/static/user/' + key + '.csv'
    db.to_csv(filename)
    return final_list

def start_collector(words,key):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    date_since = datetime.date.today()
    numtweet =50
    return scrape(words, date_since, numtweet,api,key)
