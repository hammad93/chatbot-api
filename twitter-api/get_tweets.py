import urlparse
import oauth2
import json

#Class import
from connect import oauth_req
'''
TWITTER GET HANDLE TWEETS
Hammad Usmani
Last Updated: 4/27/17

`Purpose`: Retrieve a users tweets based on a handle
`Method`: Use the Twitter REST API to retrieve tweets
`Input`: Twitter handle
`Output`: Tweets as a JSON object
`References`:
- https://dev.twitter.com/rest/reference/get/statuses/user_timeline

NOTES:
- exclude_replies is set to true by default to only retrieve handle tweets
- include_rts is set to false by default to only retrieve handle tweets
- count is set to the maximum or 200 but function iterates to max of 3200
- https://gist.github.com/yanofsky/5436496

DEBUG TEST CASE:
tweets = handle('ArianaGrande')
print len(json.loads(tweets))
print json.dumps(json.loads(tweets), indent = 4, sort_keys = True)
'''
def handle(handle, exclude_replies = 'true', include_rts = 'false', count = '200'):
    resource = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    
    #Construct request url
    url = resource
    url += '?screen_name=' + handle
    url += '&exclude_replies=' + exclude_replies
    url += '&include_rts=' + include_rts
    url += '&count=' + count
    
    #Create list and add tweets
    tweets = []
    request = json.loads(oauth_req(url))
    tweets.extend(request)
    
    while len(request) > 0 :
        #Get the id of the last element of the list so we can form the request
        oldest = tweets[-1]['id'] - 1
        
        #Make the request with the paramter max_id set to the last id
        request = json.loads(oauth_req(url + '&max_id=' + str(oldest)))
        
        #Add the request to our list of tweets
        tweets.extend(request)
    
    return tweets