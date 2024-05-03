Notes:

1. API DOC: https://timezonedb.com/api
2. no preferred db

Approach:

1. Create timezone account and get api
2. create database (will use postgres)
3. create tables(use columns provided in pdf)
4. use timezonedb for api documentation
5. to get started drop both tables on each run
    - populate timezone table with get timezone list api
    - iterate over timezone names to populate details table with timezone details api
6. pass response from api to sql fncs to insert data
7. stop dropping details table
    - check for what zones are in the details tables
    - add new params : all the zones from the timezone table and list of zones already in details tables
        - if zone is already exist skip over it

context:

1. fetch from timezonedb api
    - get list -> http://api.timezonedb.com/v2.1/list-time-zone
    - get TimeZone -> http://api.timezonedb.com/v2.1/get-time-zone
2. for get list -> params (api key)
3. for get timezone details -> params(apiKey,by:zone, zone: zoneName ) -> zoneName get from list of timeZones
4. get list response will be a json obj

Constraints:

1. **ONLY** drop timezone table on every script run
2. use primary keys given in pdf for the details table
3. no dups in timezone details, table will not be dropped
4. use get list to populate time zone table
5. use get timezone to populate zone details table
6. need to have a error log table with err msg and time stamp

SQL query to check if a timezone in the details that does not exist

```
SELECT tz.ZONENAME
FROM TZDB_TIMEZONES tz
WHERE NOT EXISTS (
    SELECT 1
    FROM TZDB_ZONE_DETAILS zd
    WHERE tz.ZONENAME = zd.ZONENAME
);
```

Questions/Notes to myself:

1. how will retrieve data from details table?
2. will I use stage table or create a list and iterate over each zone?
3. what database? (SQLITE or PostgreSQL)
4. How does the response data come back?
    - object -> will i need to convert to json
5. Remember -> SQL queries will have no other logic than querying
6. endpoints res very similar try to make it dynamic after
7. will start with single inserts try to bulk insert
