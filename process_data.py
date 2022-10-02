import json
import requests

url = "https://gbfs.divvybikes.com/gbfs/en/station_status.json"
response = requests.get(url)
stationtext = response.text
stations = json.loads(stationtext)
data = stations["data"]
stationslist = data["stations"]
bikes = 0
scooters = 0
docks = 0
for station in stationslist:
    q = station["num_bikes_available"]
    r = station.get("num_scooters_available", 0)
    s = station["num_docks_available"]
    bikes = q + bikes
    scooters = r + scooters
    docks = s + docks

print("The Number of Divvy Bikes Currently Available in Chicago: " + str(bikes))

print("The Number of Scooters Currently Available in Chicago: " + str(scooters))

print("The Number of Docks Currently Available in Chicago: " + str(docks))
