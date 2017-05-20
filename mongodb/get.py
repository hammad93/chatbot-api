from pymongo import MongoClient
from bson import ObjectId
import gridfs
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
def cache(uuid) :
    print 'getting from cache'
    #connection string
    connect = "mongodb://hammadus:7Bnf3_#99@brains-shard-00-00-yjbyo.mongodb.net:27017,brains-shard-00-01-yjbyo.mongodb.net:27017,brains-shard-00-02-yjbyo.mongodb.net:27017/brains?ssl=true&replicaSet=brains-shard-0&authSource=admin"
    
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