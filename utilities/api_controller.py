import requests
import time
from constants import api_key

# dynamic endpoint call 
def fetch_from_api(endpoint, extra_params ={}):
    parameters = {
        'key': api_key,
        'format': 'json'
    }
    parameters.update(extra_params)
    
    response = requests.get(f'http://api.timezonedb.com/v2.1/{endpoint}', params=parameters)
    
    # Need a delay to insert details to db before fetching next zone details
    # could remove by creating a list and after iteratate to insert to details table
    time.sleep(2)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to Fetch data from ' + endpoint)




