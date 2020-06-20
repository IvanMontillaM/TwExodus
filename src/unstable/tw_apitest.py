# Third party imports
import twitter

# Local application imports
import tw_config

api = twitter.Api(
    consumer_key=tw_config.consumer_key,
    consumer_secret=tw_config.consumer_secret,
    access_token_key=tw_config.access_token_key,
    access_token_secret=tw_config.access_token_secret,
    tweet_mode='extended'
)

# feed = api.GetHomeTimeline(count='75')
# feed.reverse()

# sendDM = api.PostDirectMessage('Test message', user_id=NUMBER)
