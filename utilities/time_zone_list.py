from utilities.api_controller import fetch_from_api



def get_zone_list(extra_params ={}):
    try:
       timezone_list = fetch_from_api("list-time-zone",extra_params)
       return timezone_list
    except Exception as e:
        raise(e)


