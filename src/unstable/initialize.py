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
             (user_id VARCHAR(24),
             created_at DATETIME,
             username VARCHAR(24),
             name VARCHAR(255),
             email VARCHAR(512),
             url VARCHAR(1024),
             description VARCHAR(512),
             location VARCHAR(512),
             tweets_count INT,
             following_count INT,
             followers_count INT,
             status_created_at DATETIME,
             status_full_text VARCHAR(1024),
             status_geo VARCHAR(512),
             is_verified TINYINT,
             is_protected TINYINT,
             priority INT DEFAULT 0,
             was_contacted TINYINT DEFAULT 0);''')

c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx_followers ON followers (user_id);''')

conn.commit()
conn.close()
