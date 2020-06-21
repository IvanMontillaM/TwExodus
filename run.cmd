@ECHO OFF
ECHO ----------------------------------------
ECHO TwExodus 0.0.1
ECHO ----------------------------------------
ECHO Initialize SQLite 3 Database...
.\venv\Scripts\python .\src\unstable\initialize.py
ECHO Retrieve followers online...
.\venv\Scripts\python .\src\unstable\retrieve_followers_online.py
ECHO Starting Send Mass DM...
.\venv\Scripts\python .\src\unstable\send_mass_dm.py