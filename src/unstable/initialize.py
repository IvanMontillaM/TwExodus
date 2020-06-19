# Initialization of database script

# Standard library imports
import sqlite3
import pathlib
import csv

# Local application imports
import tw_config

csv_path = pathlib.Path(__file__).parent.parent.parent.joinpath('output').as_posix() + '/'
f_csv = open(csv_path + tw_config.csv_filename, 'w', newline='')
csvf = csv.writer(f_csv)
csvf.writerow(["user_id", "message_sent"])
f_csv.close()

db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'

conn = sqlite3.connect(db_path + tw_config.db_name)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS followers
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

c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx_followers ON followers (user_id);''')

conn.commit()
conn.close()
