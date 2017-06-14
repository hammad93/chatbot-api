from pymongo import MongoClient
from bson import ObjectId
import gridfs

#connection string
connect = "mongodb://hammadus:7Bnf3_#99@brains-shard-00-00-yjbyo.mongodb.net:27017,brains-shard-00-01-yjbyo.mongodb.net:27017,brains-shard-00-02-yjbyo.mongodb.net:27017/brains?ssl=true&replicaSet=brains-shard-0&authSource=admin"

'''
Hammad Usmani
Created: 5/1/17

UPLOAD BRAIN

PURPOSE: Upload the markov chain chatbot stored in a .brain file
METHOD: Use the MongoDB Atlas driver to connect to the cloud instance and upload
using gridfs. The UUID will be included in the metadata 
INPUT: .brain file  
OUTPUT: Stored .brain in the database
References:
- https://docs.mongodb.com/manual/reference/connection-string/
- https://docs.atlas.mongodb.com/driver-connection/#python-driver-example
- https://tools.ietf.org/html/rfc4122

NOTES:
- brain is a file pointer or must have a read()
- uuid must be a string of UUID from the RFC 4122 standards. Please see reference
'''
def upload(brain, uuid, username):
    #Use connection string to connect to MongoDB atlas
    db = MongoClient(connect).brains
    #Use GridFS to store the brain file
    fs = gridfs.GridFS(db)
    
    #Create new file and upload, declaring the _id as the uuid
    fp = fs.put(brain, _uuid = uuid, _username = username)
'''
PURPOSE: Upload message to the MongoDB atlas instance brains
METHOD: Use pyMongo client to upload BSON document using insert_one
INPUT: Message needing to be inserted
'''
def message(data) :
    #Connect to the appropriate MongoDB database
    db = MongoClient(connect).brains
    
    #Insert message
    db.messages.insert_one(data)