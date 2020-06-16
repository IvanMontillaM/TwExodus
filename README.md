# TwExodus
Twitter application to mass contact your followers.

Created for balajis/twitter-export bounty. If you're @balajis I'm happy to do a Zoom Session with you to test run my tool. Just contact me at *my-GitHub-username at gmail dot com*.

## Features
- Retrieve followers and store these records in the `followers` table

## Requirements
- Basic knowledge of command line usage
- Basic knowledge of virtual environments in Python
- You must have `consumer_key` and `consumer_secret` from an already authorized application

## Instructions
1. Navigate to the cloned repository directory
2. Create a virtual environment (e.g. `$ python -m venv venv`)
3. Activate the virtual environment (e.g. `$ source venv/bin/activate`)
4. Install package requirements (e.g. `pip install -r requirements.txt`)
5. Authorize your Twitter account following these instructions: [Medium article](https://medium.com/@fbilesanmi/how-to-login-with-twitter-api-using-python-6c9a0f7165c5)
6. Duplicate file `tw_config_sample.py` into `tw_config.py` replacing with your custom values
7. Run the `initialize.py` script as this will create the empty database
8. Run the `retrieve_followers.py` script as this will populate the `followers` table with your Twitter account followers

## Implementation
- Developed with **Python 3.8.3**
- Works with **SQLite 3**
- Under `src/stable` it's where you can find the polished script (polished given time constraints, of course)

## Nice to have's for the future
- Desktop/On premises *native* application
- Markov chain or AI text generator to provide even more variety of messages to send as DMs
- Timezone detector of the follower instead of using the timezone of the main account
