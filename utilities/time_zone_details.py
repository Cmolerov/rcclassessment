from utilities.api_controller import fetch_from_api


def get_zone_details_api(zone_name):
    details_response = fetch_from_api('get-time-zone', {'by': 'zone','zone': zone_name})
    
    #datatype for zoneEnd is Number and is not nullable convert to 0 -> zoneEnd is a unix time meaning 0 has no value
    # if details_response['zoneEnd'] is None -> reassign to 0 
    # check for response status since it will return an object if the given zone is not found and will populate table 
     
    if details_response['status'] != 'FAILED':
         if details_response['zoneEnd'] is None:
            details_response['zoneEnd'] = 0
            return details_response
    else:
        raise Exception("Zone Details: " + str(details_response['message']))


def get_zone_details_db(cursor):
    # why does it come as a tuple
    try:
        cursor.execute( "SELECT ZONENAME from  TZDB_ZONE_DETAILS;")
        detail_list = cursor.fetchall()
        detail_into_list = [x[0] for x in detail_list]
        return detail_into_list
    except Exception as e:
        raise(e)
    