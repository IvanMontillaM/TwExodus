# Configuration file for TwExodus
# Customize this file and save it as "tw_config.py"

# General configurations
db_name = 'twexodus.db'  # SQLite 3 database filename
messages_filename = 'messages.txt'
csv_filename = 'messages_sent.csv'
dry_run = True  # Set to False before flight!
start_hour = 7  # Hour number in 24 hour format
end_hour = 22   # Hour number in 24 hour format
min_delay_between_dms = 35  # Minimum delay in seconds between sending DMs
max_delay_between_dms = 60  # Maximum delay in seconds between sending DMs

# Twitter API keys
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
