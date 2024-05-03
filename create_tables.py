import psycopg2

def drop_timezone_table(cursor):
    try:
        cursor.execute('DROP TABLE IF EXISTS TZDB_TIMEZONES;')
    except psycopg2.Error as e:
        print("Error dropping TZDB_TIMEZONES table:", e)

def create_timezone_table(cursor):
    
    drop_timezone_table(cursor)
    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TZDB_TIMEZONES (
                ZONENAME VARCHAR(100) PRIMARY KEY,
                COUNTRYCODE VARCHAR(2) NOT NULL,
                COUNTRYNAME VARCHAR(100) NOT NULL,
                GMTOFFSET NUMERIC,
                IMPORT_DATE TIMESTAMP
            );
        ''')
    except psycopg2.Error as e:
        print("Error creating TZDB_TIMEZONES table:", e)
        

def create_details_table(cursor):    
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TZDB_ZONE_DETAILS (
                ZONENAME VARCHAR(100),
                ZONESTART NUMERIC,
                ZONEEND NUMERIC,
                COUNTRYCODE VARCHAR(2) NOT NULL,
                COUNTRYNAME VARCHAR(100) NOT NULL,
                GMTOFFSET NUMERIC,
                DST NUMERIC,
                IMPORT_DATE TIMESTAMP,
                PRIMARY KEY (ZONENAME, ZONESTART, ZONEEND)
            );
        ''')
    except psycopg2.Error as e:
        print("Error creating TZDB_ZONE_DETAILS table:", e)

def create_error_table(cursor):
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TZDB_ERROR_LOG (
                ERROR_DATE TIMESTAMP,
                ERROR_MESSAGE VARCHAR(1000)
            );
        ''')
    except psycopg2.Error as e:
        print("Error creating TZDB_ERROR_LOG table:", e)
