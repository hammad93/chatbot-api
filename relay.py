from cobe.brain import Brain
import datetime
import os.path

#Import different classes
import sys
sys.path.append('mongodb/')
import get, put

'''
PURPOSE: retrieve the brain from the cache and download it if it isn't
METHOD: Download from mongodb atlas database
INPUT/OUTPUT: input is the uuid and output is the directory to the brain
'''
def cache(uuid) :
    directory = 'cache/' + uuid + '.brain'
    #Check if it's in our cache
    if os.path.exists(directory) :
        #It exists in our cache
        return directory
    #download from database and put into cache
    else :
        get.cache(uuid)
        return directory
'''
PURPOSE: to provide a chat relay for the chatbots
METHOD: Load brain from cache and query for message
INPUT/OUTPUT: Inputs and output are similar where they are both in this format:
    {
        'uuid' : String - UUID
        'message' : String - Message
    }
    
    Creates the entry in a journal file
'''
def chat(data) :
    directory = cache(data['uuid'])
    b = Brain(directory)
    
    reply = b.reply(data['message'])
    
    response = {
        'message' : reply,
        'uuid' : data['uuid'] 
    }
    
    #Log into our journal
    log(data, reply)
    
    return response

'''
PURPOSE: Create a log for the conversations
METHOD: Store a record in the MongoDB with all relevant fields
INPUT: The original message data and the reply from the brain. The following is
the data model for the objects to be stored in the DB:
    - Note, two of these will be stored. one for the user one for the both
    {
        timestamp : DateTime
        to : String
        from : String
        message : String
        arguments : Optional
    }
'''
def log(data, reply) :
    #Send the original message to the MongoDB
    put.message(data)
    
    #Construct the brain's reply
    document = {
        'timestamp' : str(datetime.datetime.utcnow()),
        'to' : data['from'],
        'from' : data['uuid'],
        'message' : reply
    }#No arguments
    
    #Send brains reply
    put.message(document)