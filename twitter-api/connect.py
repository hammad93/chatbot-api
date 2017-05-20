import urlparse
import oauth2
'''
TWITTER OAUTH CONNECTION
Hammad Usmani
Last Updated: 4/27/17

`Purpose`: Connect to twitter development REST API
`Method`: Use OAuth and Python to make a connection
`Input`: OAuth credentials
`Output`: Valid API calls

`References`:
- http://stackoverflow.com/questions/6399978/getting-started-with-twitter-oauth2-python
- https://dev.twitter.com/oauth
- https://dev.twitter.com/oauth/application-only
- https://github.com/joestump/python-oauth2/wiki/Twitter-Three-legged-OAuth
'''

CONSUMER_KEY = 'rbswqIgmLOxC293az9c5444zv'
CONSUMER_SECRET = 'oNyE6QQOdG9gGV3qOg4DIBJK5PdonGd8ftr3ew1sXrMZSepVoD'
ACCESS_KEY = '208775028-ZXGCwPZ5DN5auRc6rH9G1zaerE16rkKnYWCRoO4e'
ACCESS_SECRET = 'PgZStyuENCtj9fqrjDZxTENKebTn0dISPVJFw45GyvpfK'

def oauth_req(url, http_method="GET", post_body="", http_headers=None):
    
    consumer = oauth2.Consumer(key = CONSUMER_KEY, secret = CONSUMER_SECRET)
    token = oauth2.Token(key = ACCESS_KEY, secret = ACCESS_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content