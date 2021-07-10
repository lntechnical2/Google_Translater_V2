import pymongo 
import os

DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo["User"]
dbcol = db["Data"]

