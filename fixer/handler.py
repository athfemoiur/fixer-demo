import requests
import json

url = "http://data.fixer.io/api/latest?access_key="


def get_rates(api_key):
    """if successful, convert a json received from API
     to a dict and return it"""

    response = requests.get(url + api_key)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None
