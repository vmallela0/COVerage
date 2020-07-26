import requests
import ipinfo


def get_location_data():
    access_token = '99e3fb9229275a'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    location = details.loc

    latitude = location.split(',')[0]
    longitude = location.split(',')[1]

    fips_data = requests.get("https://geo.fcc.gov/api/census/area?lat=" + latitude + "&lon=" + longitude + "&format=json")
    fips_json = fips_data.json()

    return fips_json.get('results')[0]

def get_county(location_results):
    return location_results().get('county_name')

def get_fips(location_results):
    return location_results().get('county_fips')

