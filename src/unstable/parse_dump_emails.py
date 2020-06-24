# Script for exporting email addresses from direct messages

# Standard library imports
import re
import pathlib
import sqlite3
import csv

# Third party imports
import tweepy

# Local application imports
import tw_config

# Read configuration into local variables
db_name = tw_config.db_name
csv_filename = tw_config.email_csv_filename

# Authenticate to Twitter
auth = tweepy.OAuthHandler(tw_config.consumer_key, tw_config.consumer_secret)
auth.set_access_token(tw_config.access_token_key, tw_config.access_token_secret)

# Create API object
api = tweepy.API(auth)

# Pattern for finding emails
pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# Connect to database
db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'
conn = sqlite3.connect(db_path + db_name)
c = conn.cursor()

# Retrieve DMs
DMs = api.list_direct_messages()

# Oldest first, recent at the bottom
DMs.reverse()

# Retrieve, parse and update in DB
for dm in DMs:
    sender_id = dm.message_create['sender_id']
    message_text = dm.message_create['message_data']['text']
    match_str = re.search(pattern, message_text, flags=re.I | re.M | re.U)
    if match_str is not None and match_str.group(0) != '':
        email = match_str.group(0).lower()
        c.execute('''UPDATE followers SET email = ? WHERE user_id = ?;''', (email, str(sender_id)))
        conn.commit()
        print("Updated email of", sender_id, "to", email)

# Open CSV for dumping in append mode
csv_path = pathlib.Path(__file__).parent.parent.parent.joinpath('output').as_posix() + '/'
f_csv = open(csv_path + csv_filename, 'a', newline='')
csvf = csv.writer(f_csv)

rows = c.execute('''SELECT user_id, username, email FROM followers WHERE email IS NOT NULL;''')

for row in rows:
    user_id = row[0]
    username = row[1]
    email = row[2]
    csvf.writerow([user_id, username, email])

f_csv.close()
conn.commit()
conn.close()
