import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["USER"]

class Database:
