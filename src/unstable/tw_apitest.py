# Third party imports
import twitter
# import tweepy

# Local application imports
import tw_config

# Authenticate to Twitter
api = twitter.Api(
    consumer_key=tw_config.consumer_key,
    consumer_secret=tw_config.consumer_secret,
    access_token_key=tw_config.access_token_key,
    access_token_secret=tw_config.access_token_secret,
    tweet_mode='extended'
)

# # Authenticate to Twitter
# auth = tweepy.OAuthHandler(tw_config.consumer_key, tw_config.consumer_secret)
# auth.set_access_token(tw_config.access_token_key, tw_config.access_token_secret)
#
# # Create API object
# api = tweepy.API(auth)

# Create a tweet
# api.update_status("Hello Tweepy")

# feed = api.GetHomeTimeline(count='75')
# feed.reverse()

# followers = api.GetFollowers()

# sendDM = api.PostDirectMessage('Test message', user_id=NUMBER)
