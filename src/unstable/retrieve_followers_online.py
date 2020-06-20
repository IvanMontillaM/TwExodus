# Retrieval of followers online (API) and database insertion

# Standard library imports
import sqlite3
import pathlib

# Third party imports
import twitter

# Local application imports
import tw_config

db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'

conn = sqlite3.connect(db_path + tw_config.db_name)
c = conn.cursor()

api = twitter.Api(
    consumer_key=tw_config.consumer_key,
    consumer_secret=tw_config.consumer_secret,
    access_token_key=tw_config.access_token_key,
    access_token_secret=tw_config.access_token_secret,
    tweet_mode='extended'
)

followers = api.GetFollowers()

for user in followers:

    follower = (user.created_at,
                user.id_str,
                user.name,
                user.friends_count,
                user.followers_count,
                user.statuses_count,
                0,
                user.verified,
                0,
                0)

    c.execute('''INSERT OR IGNORE INTO followers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', follower)

conn.commit()
conn.close()
