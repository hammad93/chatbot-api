http://api.mongodb.com/python/current/examples/gridfs.html

###HOWTO: list all files in a db
note: in this example, we are using the db called `brains` running inside the
python shell

>>> from pymongo import MongoClient
>>> import gridfs
>>> db = MongoClient().brains
>>> fs = gridfs.GridFS(db)
>>> list(db.fs.files.find())

###HOWTO: retrieve a file based on the _id
note: the mongodb object model requires _id to by type ObjectId. We need to
import the ObjectId library
>>> from bson import ObjectId
>>> fs.get(ObjectId('#################################'))

###HOWTO: Save out the file
note: we need a GridOut object that can be obtained from a get() of a gridfs
object. see below for an example
>>> file = fs.find_one({'_uuid' : uuid})
`we are now creating our target file`
>>> fp = open('cobe.brain', 'w')
`we are now writing out to our target file`
>>> fp.write(file.read())

###HOWTO: Update a file
https://docs.mongodb.com/manual/reference/method/db.collection.update/