# rcclassessment

directions:

1. create user postgreSQL with privileges
2. create database in postgreSQL
3. create a constants.py file (follow constants_example.py)
4. in constants.py insert db_name, db_user, db_password
5. create an account in timezonedb
6. in constants.py insert api key from timezonedb
7. in terminal enter cmd : python main.py

Project Overview:

1. create a python script to query the TimeZoneDb api and populate the TZDB_TIMEZONES
   and TZDB_ZONE_DETAILS
2. The script should be able to handle errors and log them into the TZDB_ERROR_LOG table
3. The timeszones table should be deleted every time the script runs and repopulates with the data from the api
4. ZONE_DETAILS table should not be deleted, instead add data if it doesnt not exist
