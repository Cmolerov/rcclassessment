# rcclassessment

directions:

1. create user postgreSQL with privileges
2. create database in postgreSQL
3. in main.py file insert db_name, db_user, db_password
4. create an account in timezonedb
5. in api_key.py insert api key from timezonedb
6. in terminal enter cmd : python main.py

Project Overview:

1. create a python script to query the TimeZoneDb api and populate the TZDB_TIMEZONES
   and TZDB_ZONE_DETAILS
2. The script should be able to handle errors and log them into the TZDB_ERROR_LOG table
3. The timeszones table should be deleted every time the script runs and repopulates with the data from the api
4. ZONE_DETAILS table should not be deleted, instead add data if it doesnt not exist
