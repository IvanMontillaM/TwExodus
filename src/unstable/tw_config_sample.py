# Configuration file for TwExodus
# Customize this file and save it as "tw_config.py"

# General configurations
db_name = 'twexodus.db'  # SQLite 3 database filename
messages_filename = 'messages.txt'  # Direct Message texts you'll be sending
follower_filename = 'follower.js'  # Your offline followers file from Twitter archive (optional)
msg_csv_filename = 'messages_sent.csv'  # CSV file for sent DMs to which user ID
email_csv_filename = 'email_dump.csv'  # CSV file for extracted emails
dry_run = True  # Set to False before flight!
start_hour = 7  # Hour number in 24 hour format
end_hour = 22   # Hour number in 24 hour format
min_delay_between_dms = 35  # Minimum delay in seconds between sending DMs
max_delay_between_dms = 60  # Maximum delay in seconds between sending DMs

# Twitter API keys
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'  # Consumer Key from your authorized application
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'  # Consumer Secret from your authorized application
access_token_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'  # Access Token from your authorized account
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'  # Access Secret from your authorized account
