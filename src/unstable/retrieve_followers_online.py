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

    follower = ()
    try:
        c.execute('''INSERT INTO followers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0, 0);''',
                  (user.id_str,
                   user.created_at,
                   user.screen_name,
                   user.name,
                   user.email,
                   user.url,
                   user.description,
                   user.location,
                   user.statuses_count,
                   user.friends_count,
                   user.followers_count,
                   str(user.status.created_at if hasattr(user.status, "created_at") else ''),
                   str(user.status.full_text if hasattr(user.status, "full_text") else ''),
                   str(user.status.geo if hasattr(user.status, "geo") else ''),
                   user.verified,
                   user.protected))
    except sqlite3.IntegrityError:
        c.execute('''UPDATE followers SET 
                  created_at = ?,
                  username = ?,
                  name = ?,
                  url = ?,
                  description = ?,
                  location = ?,
                  tweets_count = ?,
                  following_count = ?,
                  followers_count = ?,
                  status_created_at = ?,
                  status_full_text = ?,
                  status_geo = ?,
                  is_verified = ?,
                  is_protected = ?
                  WHERE user_id = ?;''',
                  (user.created_at,
                   user.screen_name,
                   user.name,
                   user.url,
                   user.description,
                   user.location,
                   user.statuses_count,
                   user.friends_count,
                   user.followers_count,
                   str(user.status.created_at if hasattr(user.status, "created_at") else ''),
                   str(user.status.full_text if hasattr(user.status, "full_text") else ''),
                   str(user.status.geo if hasattr(user.status, "geo") else ''),
                   user.verified,
                   user.protected,
                   user.id_str))
    except Exception as e:
        print("Could not", str(e), user.screen_name)


conn.commit()
conn.close()
