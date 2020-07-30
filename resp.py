import requests

def get_location_data(lat, long):
    location = details.loc

    latitude = location.split(',')[0]
    longitude = location.split(',')[1]

    fips_data = requests.get("https://geo.fcc.gov/api/census/area?lat=" + lat + "&lon=" + long + "&format=json")
    fips_json = fips_data.json()

    return [fips_json.get('results')[0].get('county_name'), fips_json.get('results')[0].get('county_fips')]

