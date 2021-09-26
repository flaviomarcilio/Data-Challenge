from parts.secrets import MONGO_HOST, MONGO_PASSWORD, MONGO_USERNAME
from pymongo import MongoClient

uri = "mongodb+srv://%s:%s@%s" % (MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST)

client = MongoClient(uri)

db = client.data_challenge

trends_collection = db.trends
tweets_collection = db.tweets
