from cobe.brain import Brain
import json
import uuid

#import twitter-api classes
import sys
sys.path.append('../twitter-api/')
sys.path.append('../mongodb/')

import connect, get_tweets, parse_tweets    #Twitter API
import get, put                             #MongoDB

'''
CREATE CHATBOT BRAIN
Hammad Usmani
Created: 4/28/17

`Purpose`: Create a markov chain chatbot with a user's tweets for the corpus
`Method`: Use the open source library called cobe and the Twitter API to 
generate chatbots. Upload to the local mongodb database
`Input`: Twitter handle and username associated with chatbot
`Output`: a ".brain" file with a UUID as the file name 

`References`:
- https://github.com/pteichman/cobe
- https://github.com/pteichman/cobe/wiki/Getting-started
- https://docs.python.org/2/library/uuid.html

NOTES:
- UUID
    - each brain is named with a randomly generated UUID with RFC 4122 standards
    - to return in the prober hex string format, use uuid.hex
'''
def twitter(handle, username, directory = ""):
    #Generate UUID as string
    UUID = uuid.uuid4().hex
    
    #Create brain
    name = directory + UUID + '.brain'
    b = Brain(name)
    
    #Get twitter corpus from available REST API based on user handle as a list
    corpus = parse_tweets.parse(handle)
    
    #Iterate through corpus list and learn each parsed tweet
    for tweet in corpus :
        b.learn(tweet['text-parsed'])
    
    #Create a file pointer to the brain for upload 
    fp = open(name, 'r')
    put.upload(fp, UUID, username)
    fp.close()
    
    #Return our identifier
    return UUID