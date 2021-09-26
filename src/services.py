from datetime import datetime
from typing import List, Dict, Any

import tweepy

from src.connection import trends_collection, tweets_collection
from src.constants import BRAZIL_WOE_ID
from parts.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET


def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:
    """Get trending topics.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    trends = api.trends_place(woe_id)

    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trends() -> List[Dict[str, Any]]:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)
    return trends


def _get_tweets(keyword: str, count: int, result_type: str,
                lang: str, tweet_mode: str, api: tweepy.API) -> List[Dict[str, Any]]:
    tweets_iterator = tweepy.Cursor(api.search, q=keyword, tweet_mode=tweet_mode,
                                    rpp=count, result_type=result_type,
                                    since=datetime(2021, 9, 20, 0, 0, 0).date(),
                                    lang=lang, include_entities=True).items(count)

    tweets_list = []
    for tweet in tweets_iterator:
        if 'retweeted_status' not in dir(tweet):
            tweet_text = tweet.full_text
            tweets_data = {
                'ID': tweet.id,
                'TweetText': tweet_text,
                'Date': tweet.created_at,
                'Source': tweet.source,
                'Likes': tweet.favorite_count,
                'Retweets': tweet.retweet_count
            }

            tweets_list.append(tweets_data)

    return tweets_list


def get_tweets_from_mongo(keyword: str) -> List[Dict[str, Any]]:
    tweets = tweets_collection.find({"keyword": keyword})
    return tweets[0]["tweets"]


def save_tweets(keyword: str) -> List[Dict[str, Any]]:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    tweets = _get_tweets(keyword=keyword,
                         count=50,
                         result_type='mixed',
                         lang='en',
                         tweet_mode='extended',
                         api=api)

    post = {"keyword": keyword,
            "tweets": tweets}

    tweets_collection.insert_one(post)

    return tweets
