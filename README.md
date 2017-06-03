# chatbot-api
## Documentation
`note: the server uses swagger.io to automatically generate documentation. Please
visit the home directory for automatically generated documentation.`

References: 

http://swagger.io/swagger-ui/

## Quick Start
* Install proper dependencies and execute the command `sudo python api.py`

### Endpoints
`/api/` : home directory

`/api/create/` : CRUD command

`/api/read/` : CRUD command

`/api/update/` : CRUD command

`/api/delete/` : CRUD command

`/api/list/` : CRUD command

`/chat/` : chat relay

## CREATE
`PURPOSE:` To create a chatbot and store it into the MongoDB database

`INPUT:` Request JSON requires these parameters:
    - username
    - twitter handle
    
`OUTPUT:` The UUID of the chatbot
## READ
`PURPOSE:` To return a binary file containing the .brain of the chatbot

`INPUT:` Request JSON requires these parameters:
    - UUID
    
`OUTPUT:` .brain file
## UPDATE
`PURPOSE:` Update a chatbot

`INPUT:` Request JSON with these parameters:
    - Chatbot UUID
    - .brain file
    
`OUTPUT:` UUID of the updated chatbot
## DELETE
`PURPOSE:` Delete a chatbot

`INPUT:` Request JSON with these parameters:
    - Chatbot UUID
    
`OUTPUT:` UUID of deleted chatbot
## LIST
`PURPOSE:` List the chatbots for a username

`INPUT:` Request JSON with these parameters:
    - username
    
`OUTPUT:` List of Chatbot UUID's

### NOTES:
- flask-restplus vs connexion: flask-restplus was chosen because it has the MIT
license instead of the Apache 2.0 license in connexion. Both are equivalent
- Server IP: 104.154.217.7