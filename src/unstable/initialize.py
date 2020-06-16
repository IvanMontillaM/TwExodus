# Initialization of database script

# Standard library imports
import sqlite3
import pathlib

# Local application imports
import tw_config

db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'

conn = sqlite3.connect(db_path + tw_config.db_name)
c = conn.cursor()

c.execute('''CREATE TABLE followers
             (created_at DATETIME,
             user_id VARCHAR(24),
             username VARCHAR(24),
             following_count INT,
             followers_count INT,
             tweets_count INT,
             priority INT,
             is_verified TINYINT,
             was_contacted TINYINT,
             text_id INT);''')

c.execute('''CREATE UNIQUE INDEX idx_followers ON followers (user_id);''')

conn.commit()
conn.close()
