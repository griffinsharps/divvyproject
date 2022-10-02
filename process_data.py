import json

f = open("stations.json")
stationtext = f.read()
stations = json.loads(stationtext)
data = stations["data"]
stationslist = data["stations"]
sum = 0
for station in stationslist:
    q = station["num_bikes_available"]
    sum = q + sum

print("The Number of Divvy Bikes Currently Available in Chicago: " + str(sum))

sum = 0
for station in stationslist:
    r = station.get("num_scooters_available", 0)
    sum = r + sum

print("The Number of Scooters Currently Available in Chicago: " + str(sum))

sum = 0
for station in stationslist:
    s = station["num_docks_available"]
    sum = s + sum

print("The Number of Docks Currently Available in Chicago: " + str(sum))