#TWITTER API INTEGRATION

###Twitter OAuth Connection (connect.py)
`Purpose`: Connect to twitter development REST API
`Method`: Use OAuth and Python to make a connection
`Input`: OAuth credentials
`Output`: Valid API calls
`References`:
- http://stackoverflow.com/questions/6399978/getting-started-with-twitter-oauth2-python
- https://dev.twitter.com/oauth
- https://dev.twitter.com/oauth/application-only
- https://github.com/joestump/python-oauth2/wiki/Twitter-Three-legged-OAuth

###Twitter Get Handle Tweets (get_tweets.py)
`Purpose`: Retrieve a users tweets based on a handle
`Method`: Use the Twitter REST API to retrieve tweets
`Input`: Twitter handle
`Output`: Tweets as a JSON object
`References`:
- https://dev.twitter.com/rest/reference/get/statuses/user_timeline

###Parse tweets (parse_tweets.py)
`Purpose`: Parse tweets based on response and filters
`Method`: Retrieve tweet JSON object and access tweets for parsing
`Input`: user handle
`Output`: Parsed Tweets as a JSON object
`References`:

#Regex
removing @:
@([a-zA-Z0-9\_\.]+)

..[1-9]

^[(http)(https)]://