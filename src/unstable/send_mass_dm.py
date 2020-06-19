# Send Mass DMs script

# Standard library imports
import time
import csv
import pathlib
import sys
import random
import sqlite3

# Third party imports
import twitter

# Local application imports
import tw_config

# Read configuration into local variables
db_name = tw_config.db_name
messages_filename = tw_config.messages_filename
csv_filename = tw_config.csv_filename
dry_run = tw_config.dry_run
start_hour = tw_config.start_hour
end_hour = tw_config.end_hour
min_delay_between_dms = tw_config.min_delay_between_dms
max_delay_between_dms = tw_config.max_delay_between_dms

hour_now = time.localtime().tm_hour
pending_work_hours = end_hour - hour_now

# Too late to run for today, kill script
if pending_work_hours <= 0:
    sys.exit()

dms_left_to_send = 60 * pending_work_hours

msg_path = pathlib.Path(__file__).parent.parent.parent.joinpath('input').as_posix() + '/'
f_msg = open(msg_path + messages_filename, 'r', newline='')
messages = f_msg.readlines()
f_msg.close()
lines_count = len(messages)

csv_path = pathlib.Path(__file__).parent.parent.parent.joinpath('output').as_posix() + '/'

f_csv = open(csv_path + csv_filename, 'a', newline='')
csvf = csv.writer(f_csv)

db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'

conn = sqlite3.connect(db_path + db_name)
c = conn.cursor()

rows = c.execute('''SELECT user_id FROM followers WHERE was_contacted = 0 ORDER BY priority DESC LIMIT ?;''',
                 (str(dms_left_to_send),))

for row in rows:
    user_id = row[0]
    message = messages[random.randint(0, lines_count-1)].strip()
    print('Tweet to send:', row[0], message)
    csvf.writerow([user_id, message])
    # if dry_run == False:
    #     actually-send-the-dm()
    # ---------------------------- FIX WEIRD BUG HERE -------------------------------------------
    # c.execute('''UPDATE followers SET was_contacted = 1 WHERE user_id = ?;''', (str(user_id),))
    # conn.commit()
    # ---------------------------- FIX WEIRD BUG HERE -------------------------------------------
    seconds_to_sleep = random.randint(min_delay_between_dms, max_delay_between_dms)
    print('Seconds to sleep:', seconds_to_sleep)
    # time.sleep(seconds_to_sleep)

f_csv.close()
conn.commit()
conn.close()
