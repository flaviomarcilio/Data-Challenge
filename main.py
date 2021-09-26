from typing import List

import uvicorn

from fastapi import FastAPI

from src.services import get_trends_from_mongo, save_trends, get_tweets_from_mongo, save_tweets
from src.responses import TrendItem, TweetItem

app = FastAPI()


@app.get("/trends", response_model=List[TrendItem])
def get_trends_route():
    trends = get_trends_from_mongo()
    if not trends:
        trends = save_trends()
    return trends


@app.get("/tweets/{keyword}", response_model=List[TweetItem])
def get_tweets_route(keyword: str):
    tweets = get_tweets_from_mongo(keyword=keyword)
    if not tweets:
        return save_tweets(keyword=keyword)

    return tweets


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)