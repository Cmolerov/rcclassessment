import psycopg2
from create_tables import create_error_table,create_details_table,create_timezone_table
from sql_queries import insert_error, insert_timezones_list, insert_zone_details
from utilities.time_zone_details import get_zone_details_api, get_zone_details_db
from utilities.time_zone_list import get_zone_list
from constants import DB_HOST,DB_NAME, DB_USER, DB_PASSWORD


if __name__ == '__main__':
    # create if it doesnt exist or connect to existing db 
    try:
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        cursor = conn.cursor()
    except Exception as e:
        print("Database Error: UNABLE TO CONNECT TO DATABASE: ", e)
        # Exit the script if unable to connect to the database
        exit(1)

    # create tables -> in create_timezone_table it will be drop if it exist each time the script runs 
    try:
        create_timezone_table(cursor)
        create_details_table(cursor)
        create_error_table(cursor)
        conn.commit()
    except Exception as e:
        insert_error("Error creating tables:" + str(e), cursor, conn)

    # fetch time zone list and insert to timezones table
    try:
        time_zone_list_response = get_zone_list()
        insert_timezones_list(time_zone_list_response, cursor, conn)
    except Exception as e:
        insert_error("Error with get time zone list or data insertion: " + str(e) , cursor, conn)
      
      
    # retrieve data from db & iterate zone list, if it does not exist fetch zone details 
    # & insert to details table else skip to next zone (no replacing)
    try:
        zone_details_from_db = get_zone_details_db(cursor)
        for zone in time_zone_list_response['zones']:
            if zone['zoneName'] in zone_details_from_db:
                continue
            details_response = get_zone_details_api(zone['zoneName'])
            insert_zone_details(details_response, cursor, conn)
    except Exception as e:
        insert_error("Error in Zone Details " + str(e), cursor, conn)
    
    conn.commit()
    print('Script has Finished Running')

