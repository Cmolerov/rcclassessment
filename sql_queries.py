from datetime import datetime
import psycopg2

# place rollback due to any errors that would block commiting zones list to the db 
# would cause a rollback on transaction blocking inserting error to err log table

def insert_error(message,c,conn):
    try:
        time_now = datetime.now()
        c.execute(f''' 
                INSERT INTO TZDB_ERROR_LOG 
                (ERROR_DATE, ERROR_MESSAGE)
                VALUES
                ( '{time_now}','{message}');
                ''')
        conn.commit()
    except Exception as e:
        print("Error inserting to Error table: ",e)

def insert_timezones_list(json_response, c,conn):
    time_now = datetime.now()
    try:
        for res in json_response['zones']:
            c.execute(f'''
            INSERT INTO TZDB_TIMEZONES
            (COUNTRYCODE, COUNTRYNAME, ZONENAME, GMTOFFSET, IMPORT_DATE)
            VALUES
            ('{res['countryCode']}', '{res['countryName']}', '{res['zoneName']}', 
             {res['gmtOffset']}, '{time_now}');
            ''')
    except psycopg2.Error as e:
        conn.rollback()
        insert_error('Error Inserting into TZDB_TIMEZONES: ' +str(e), c,conn)



def insert_zone_details(details_response, c,conn):
    time_now = datetime.now()
    try:
        c.execute(f'''
        INSERT INTO TZDB_ZONE_DETAILS 
        (ZONENAME,ZONESTART,ZONEEND,COUNTRYCODE,
            COUNTRYNAME ,GMTOFFSET ,DST,IMPORT_DATE)
            VALUES
            ( '{details_response['zoneName']}', '{details_response['zoneStart']}', '{details_response['zoneEnd']}',
            '{details_response['countryCode']}', '{details_response['countryName']}', '{details_response['gmtOffset']}',
            '{details_response['dst']}', '{time_now}' );''')
        conn.commit()
    except psycopg2.Error as e:
        insert_error('Error Inserting into TZDB_ZONE_DETAILS: ' +str(e), c,conn)


     
