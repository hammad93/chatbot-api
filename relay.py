from cobe.brain import Brain
import datetime
import os.path

#Import different classes
import sys
sys.path.append('mongodb/')
import get

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
    
    
    return response

'''
PURPOSE: Create a log for the conversations
METHOD: Open up the journal file for the associated brain
INPUT/OUPUT: The UUID for the brain, the message, and the brain response
    Structure of journal file (identifier's are encapsulated by ``) -
    [`DATETIME`] [`BRAIN OR USER?`] : `REPLY`
    
    Example:
    [2017-06-02 19:27:07] [BRAIN] : hello!
    [2017-06-02 19:27:08] [USER] : hi!
'''
def log(uuid, message, reply) :
    #Directory of the brain journal
    directory = 'cache/' + uuid + '.brain-journal'
    
    #Open journal
    fp = open(directory, 'w')
    
    #Write to journal
    fp.write()
    
    #Close journal and finalize
    fp.close()