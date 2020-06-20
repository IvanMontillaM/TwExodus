# Retrieval of followers offline (JSON file) and database insertion

# Standard library imports
import sqlite3
import pathlib
import json

# Local application imports
import tw_config

db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('db').as_posix() + '/'

conn = sqlite3.connect(db_path + tw_config.db_name)
c = conn.cursor()

fw_path = db_path = pathlib.Path(__file__).parent.parent.parent.joinpath('input').as_posix() + '/'
fw = open(fw_path + tw_config.follower_filename, 'r', newline='')

fw_lines = fw.readlines()
fw_lines[0] = "[ {"
fw_lines = ''.join(fw_lines)

fw_json = json.loads(fw_lines)

for fw in fw_json:
    c.execute('''INSERT OR IGNORE INTO followers VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);''',
              (fw['follower']['accountId'],))

conn.commit()
conn.close()
