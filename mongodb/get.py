from pymongo import MongoClient
from bson import ObjectId, Binary, Code, json_util
import gridfs
import json
'''
commands to upload and download the file -
#connection string
connect = "mongodb://hammadus:7Bnf3_#99@brains-shard-00-00-yjbyo.mongodb.net:27017,brains-shard-00-01-yjbyo.mongodb.net:27017,brains-shard-00-02-yjbyo.mongodb.net:27017/brains?ssl=true&replicaSet=brains-shard-0&authSource=admin"

#Use connection string to connect to MongoDB atlas
db = MongoClient(connect).brains
#Use GridFS to store the brain file
fs = gridfs.GridFS(db)

#this downloads a ariana grande bot or you can find another one with a uuid
file = fs.fine_one({'_uuid' : '5ef04c3c9a3b4a2c8b31745bd09091ed'})

#create our output file
fp = open('cobe.brain', 'w')

#write it output
fp.write(file.read())
'''
#Global Connection String
connect = "mongodb://hammadus:7Bnf3_#99@brains-shard-00-00-yjbyo.mongodb.net:27017,brains-shard-00-01-yjbyo.mongodb.net:27017,brains-shard-00-02-yjbyo.mongodb.net:27017/brains?ssl=true&replicaSet=brains-shard-0&authSource=admin"

def cache(uuid) :
    #Use connection string to connect to MongoDB atlas
    db = MongoClient(connect).brains
    #Use GridFS to store the brain file
    fs = gridfs.GridFS(db)
    
    #this downloads the brain associated with the uuid
    file = fs.find_one({'_uuid' : uuid})
    
    #create our output file
    fp = open('cache/' + uuid + '.brain', 'w')
    
    #write it output
    fp.write(file.read())
    
    #close out and return uuid
    fp.close()
    
    return uuid
'''
PURPOSE: To get the chat logs of a chatbot
METHOD: Get from MongoDB brains messages collection
INPUT: The uuid associated with the chatbot and the limit of messages (by
default 10)
OUTPUT: The BSON documents serialized into JSON for the chat records
'''
def log(uuid, limit = 10) :
    #Use connection string to connect to MongoDB Atlas
    db = MongoClient(connect).brains
    
    #Connect to messages
    collection = db.messages
    
    #Send query for all relevant messages with the uuid
    response = collection.find({'uuid' : uuid}).limit(limit)
    
    #Send back response as list
    return json.loads(json_util.dumps(response))
'''
PURPOSE: To return all the chatbot uuid's associated with a username
METHOD: Go into GridFS and query the username
INPUT: Username
OUTPUT: Array of UUID's
'''
def uuids(username) :
    #Use connection string to connect to MongoDB atlas
    db = MongoClient(connect).brains
    
    #query for responses
    response = db.fs.files.find({'_username':  username})
    
    #Send back as JSON object
    return json.loads(json_util.dumps(response))