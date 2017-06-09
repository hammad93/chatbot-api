import json
from flask import Flask, request
from flask_restplus import Resource, Api, fields, reqparse
import datetime
#Default import from current directory
import relay

#Import different classes
import sys
sys.path.append('create-bot/')
sys.path.append('mongodb/')
sys.path.append('twitter-api/')

import create as spawn
import get, put

'''
CHATBOT REST API
Hammad Usmani
Created: 4/28/17

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
API MODEL DECLARATIONS
The following are the models for the appropriate api resources
'''
chat_model = api.model('chat_model', {
    'timestamp' : fields.DateTime(description = 'The date and time in ISO 8601 (YYYY-MM-DDThh:mm:ss.sTZD) format that the message was sent. Please use seconds where applicable',
                required = True, example = str(datetime.datetime.utcnow())),
    'from' : fields.String(description = 'The identifier for the object sending the message. This can be the username or uuid',
                required = True, example = "hammadus"),
    'uuid' : fields.String(description = 'The identifier for the object receiving the message. This can be the username or uuid', 
                required = True, example = '62aeb372539b4aee92ff946de2e6c4ab'),
    'message' : fields.String(description = 'The message being sent', required = True, example = 'hello ! <3'),
    'arguments' : fields.List(fields.String, description = 'Optional field for any additional arguments. Arguments are strings',
                required = False)
})

create_model = api.model('create_model', {
    'timestamp' : fields.DateTime(description = 'The date and time in ISO 8601 (YYYY-MM-DDThh:mm:ss.sTZD) format that the message was sent. Please use seconds where applicable',
                required = True, example = str(datetime.datetime.utcnow())),
    'username' : fields.String(description = 'The identifier for the object sending the message. This can be the username or uuid',
                required = True, example = "hammadus"),
    'arguments' : fields.List(fields.String, description = "Arguments for creating the chatbot. Please use double quotes", example = '{"handle":"ArianaGrande"}')
})
'''
#CHAT RELAY

PURPOSE: To provide a chat relay for the chatbots in the database
METHOD: Use a markov-chain chatbot to create artificial intelligence using the
method created by Peter Teichmcd

INPUT/OUTPUT: Based on the message relay some data, the output will follow the
chat_model 

REFERENCES:
- https://github.com/pteichman
'''
@api.route('/chat')
class chat(Resource):
    @api.doc(description = 'This resource chats with the brain associated with the uuid that are housed in MongoDB Atlas')
    @api.expect(chat_model)
    def post(self):
        #return chat response
        return relay.chat(api.payload)
'''
## CREATE
`PURPOSE:` To create a chatbot and store it into the MongoDB database

`INPUT:` Request JSON requires these parameters:
    - username          #Stored in the metadata for the .brain file
    - twitter handle    #Stored in the metadata for the .brain file
    
`OUTPUT:` The UUID of the chatbot
'''
@api.route('/api/create')
class create(Resource):
    @api.doc(description = 'If you are creating using a twitter handle, make sure to ommit the @')
    @api.expect(create_model)
    def post(self):
        #Assign payload
        data = api.payload
        
        #Find handle from arguments
        twitter = json.loads(data['arguments'][0])
        
        #Create chatbot based on parameters
        return spawn.twitter(twitter['handle'], data['username'], "cache/")
'''
## READ
`PURPOSE:` To return a response containing the chat log of the chatbot

`INPUT:` Request JSON requires these parameters:
    - UUID
    
`OUTPUT:` Array of BSON objects
'''
@api.route('/api/read')
@api.doc(description = 'The resource to get the chatlogs', params={
                'uuid': 'The identifier for the chatbot in the query', 
                'limit' : 'The limit of the number of requests to receive'})
class read(Resource):
    def get(self):
        #declare parser attributes
        parser = reqparse.RequestParser()
        parser.add_argument('uuid', action='append')
        parser.add_argument('limit', action='append', type = int)
        
        #Get data from request
        response = parser.parse_args()
        
        #Format the response data
        data = {
            'uuid' : response['uuid'][0],
            'limit' : response['limit'][0]
        }
        
        #Set limit if there's none
        if data['limit'] is None :
            data['limit'] = 10
        
        return get.log(data['uuid'], data['limit'])
'''
## LIST
`PURPOSE:` List the chatbots for a username

`INPUT:` Request JSON with these parameters:
    - username
    
`OUTPUT:` List of Chatbot UUID's
'''
@api.route('/api/list')
@api.doc(description = 'The resource to get the uuids of a user', params={
                'username': 'The username to query for'})
class list(Resource):
    def get(self):
        #declare parser attributes
        parser = reqparse.RequestParser()
        parser.add_argument('username', action='append')
        
        #Get data from request
        response = parser.parse_args()
        
        #Format the response data
        data = {
            'username' : response['username'][0]
        }
        return get.uuids(data['username'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)