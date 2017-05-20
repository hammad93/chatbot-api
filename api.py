import json
from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse
#Default import from current directory
import relay

#Import different classes
import sys
sys.path.append('create-bot/')
sys.path.append('mongodb/')
sys.path.append('twitter-api/')

import create as birth
import get, put

'''
CHATBOT REST API
Hammad Usmani
Last Updated: 5/16/17

PURPOSE: To provide a REST API for create, read, update, delete, and list (CRUD) 
operations on the MongoDB .brain files
METHOD: Using flask as the server and OpenAPI for specifications, we can provide
a HTTP REST API to perform CRUD operations and chatting

REFERENCES:
- https://github.com/noirbizarre/flask-restplus
- http://flask-restplus.readthedocs.io/en/stable/index.html
- http://swagger.io/swagger-ui/
- https://flask-restplus.readthedocs.io/en/stable/example.html

NOTES:
- Server automatically generates API documentation. To view the documentation, 
navigate to the specified directory for specifications according to OpenAPI. By
default this is the root director
'''
app = Flask(__name__)
api = Api(app, version='1.0', title='Chatbot API', description='OpenAPI')
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
app.config.SWAGGER_UI_JSONEDITOR = True

'''
#CHAT RELAY

PURPOSE: To provide a chat relay for the chatbots in the database
METHOD: Use a markov-chain chatbot to create artificial intelligence using the
method created by Peter Teichmcd cache


INPUT/OUTPUT: Based on the message relay some data, the output will be as follows -
Both input and output are in the same format. Timestamp is in ISO 8601 and time region is UTC
message: application/json
    {
        'message': string    #Content of the message. Can have JSON strings
        'uuid': UUID      #The index for the bot in a hex UUID formatted string
    }
NOTE: Output will be a string

REFERENCES:
- https://github.com/pteichman

data = json.loads(json.dumps(request.get_json(force=True)))
'''
@api.route('/chat')
@api.doc(params={'uuid': 'The UUID associated with the chatbot', 'message': 'The message to relay to the chatbot'})
class chat(Resource):
    def get(self):
        #declare parser attributes
        parser = reqparse.RequestParser()
        parser.add_argument('uuid', action='append')
        parser.add_argument('message', action='append')
        
        #Get data from request
        response = parser.parse_args()
        #Format the response data
        data = {
            'uuid' : response['uuid'][0],
            'message' : response['message'][0]
        }
        
        #return chat response
        return relay.chat(data)
'''
## CREATE
`PURPOSE:` To create a chatbot and store it into the MongoDB database

`INPUT:` Request JSON requires these parameters:
    - username          #Stored in the metadata for the .brain file
    - twitter handle    #Stored in the metadata for the .brain file
    
`OUTPUT:` The UUID of the chatbot
'''
@api.route('/api/create')
@api.doc(params={'username': 'An ID', 'handle': 'Twitter Handle'})
class create(Resource):
    
    def get(self):
        #declare parser attributes
        parser = reqparse.RequestParser()
        parser.add_argument('username', action='append')
        parser.add_argument('handle', action='append')
        
        #Get data from request
        data = parser.parse_args()
        
        #Create chatbot based on parameters
        return birth.twitter(data['handle'][0], data['username'][0], "cache/")
'''
## READ
`PURPOSE:` To return a binary file containing the .brain of the chatbot

`INPUT:` Request JSON requires these parameters:
    - UUID
    
`OUTPUT:` .brain file
'''
@api.route('/api/read')
@api.doc(params={'id': 'An ID'})    
class read(Resource):
    def get(self, id):
        return id

'''
## UPDATE
`PURPOSE:` Update a chatbot

`INPUT:` Request JSON with these parameters:
    - Chatbot UUID
    - .brain file
    
`OUTPUT:` UUID of the updated chatbot
'''
@api.route('/api/update')
@api.doc(params={'id': 'An ID'})    
class update(Resource):
    def get(self, id):
        return id

'''
## DELETE
`PURPOSE:` Delete a chatbot

`INPUT:` Request JSON with these parameters:
    - Chatbot UUID
    
`OUTPUT:` UUID of deleted chatbot
'''
@api.route('/api/delete')
@api.doc(params={'id': 'An ID'})    
class delete(Resource):
    def get(self, id):
        return id

'''
## LIST
`PURPOSE:` List the chatbots for a username

`INPUT:` Request JSON with these parameters:
    - username
    
`OUTPUT:` List of Chatbot UUID's
'''
@api.route('/api/list')
@api.doc(params={'id': 'An ID'})    
class list(Resource):
    def get(self, id):
        return id


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)