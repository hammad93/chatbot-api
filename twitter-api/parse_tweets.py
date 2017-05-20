import json
import preprocessor as p

#Import twitter-api class modules
import get_tweets
'''
PARSE TWEETS
Hammad Usmani 
Last Updated: 4/28/17

`Purpose`: Parse tweets based on response and filters
`Method`: Retrieve tweet JSON object and access tweets for parsing. We will be 
using the python library called tweet-preprocessor to parse the tweets
`Input`: JSON Object containing tweets according to Twitter API
`Output`: Parsed Tweets as a JSON object
`References`:
- https://dev.twitter.com/rest/reference/get/statuses/user_timeline
- https://dev.twitter.com/rest/public/timelines
- https://www.analyticsvidhya.com/blog/2015/06/quick-guide-text-data-cleaning-python/
- https://github.com/s/preprocessor
'''
def parse(handle):
    #Request tweets from handle and store as a list
    tweets = get_tweets.handle(handle)
    
    #Iterate through the texts of each tweet and filter and censor if applicable
    for tweet in tweets:
        text = tweet['text']
        
        #Remove hashtags, links, and mentions
        p.set_options(p.OPT.URL, p.OPT.MENTION)
        text = p.clean(text)
        
        #Add the parsed tweet text back into the tweet object
        tweet['text-parsed'] = text
    
    return tweets