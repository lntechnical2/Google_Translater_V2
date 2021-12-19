import pymongo 
import os

DB_NAME = os.environ.get("DB_NAME","")
DB_URL = os.environ.get("DB_URL","")
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["USER"]

def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id,"lg_code":None}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def set(chat_id,lg_code):
	 dbcol.update_one({"_id":chat_id},{"$set":{"lg_code":lg_code}})

	 	
def unset(chat_id):
	dbcol.update_one({"_id":chat_id},{"$set":{"lg_code":None}})

def find(chat_id):
	id =  {"_id":chat_id}
	x = dbcol.find(id)
	for i in x:
             lgcd = i["lg_code"]
             return lgcd 

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values

def find_one(id):
	return dbcol.find_one({"_id":id})
