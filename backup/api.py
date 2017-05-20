from flask import Flask, request
from cobe.brain import Brain

import json
import datetime

app = Flask(__name__)

'''
STANDARD API HOME MESSAGE
'''
@app.route('/')
def index():
    return "Please reference API documentation"

'''
PURPOSE: Provide the api for the chatbot
METHOD: Using HTTP for the REST API requests
OUTPUT: Based on the message send the API, the output will be as follows - 
    Both input and output are in the same format. Timestamp is in ISO 8601
    and time region is UTC
    https://www.iso.org/iso-8601-date-and-time-format.html
    message: `json`
        - json format:
        {
            'timestamp': YYYY-MM-DDThh:mm:ssTZD (UTC)
            'to': string
            'from': string
            'message': string
            'bot-id': string
        }
    output:
        - json format:
        {
            'timestamp': YYYY-MM-DDThh:mm:ssTZD (UTC)
            'to': string
            'from': string
            'message': string
            'bot-id': string
        }
    NOTE: Output will be a string
'''
@app.route(u'/api/<path:message>', methods=['GET', 'POST'])
def reply(message):
    
    #For an api request on `reply` send back the proper JSON object
    if message == 'chat':
        #get json request from POST into proper dictionary
        data = json.loads(json.dumps(request.get_json(force=True)))
        
        #get the message to perform chat
        message = data['message']
        
        #Create the brain instance
        b = Brain('cobe.brain')
        #create the reply
        reply = b.reply(message)
        
        '''
        WARNING: NEEDS UPDATE
        FORMAT RESPONSE BELOW
        '''
        response = {
            "timestamp" : str(datetime.datetime.utcnow()),
            "to" : data['from'],
            "from" : data['to'],
            "message" : reply,
            "bot-id" : data['bot-id']
        }
        
        #send the response in json
        return json.dumps(response)
        
if __name__ == '__main__':
    #app should be run on 0.0.0.0 to allow remote http requests
    app.run(host='0.0.0.0', debug=True, port=80)