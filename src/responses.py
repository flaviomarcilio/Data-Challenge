import datetime

from pydantic import BaseModel


class TrendItem(BaseModel):
    name: str
    url: str


class TweetItem(BaseModel):
    ID: int
    TweetText: str
    Date: datetime.datetime
    Source: str
    Likes: int
    Retweets: int
