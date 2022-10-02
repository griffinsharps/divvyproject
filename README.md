# divvyproject
How many bikes, scooters, and docks are available in Chicago's Divvy bike system right now?
We can answer this question using Lyft's real-time [Divvy API](https://ride.divvybikes.com/system-data).

This project uses Python to fetch data from Divvy's station info [GBTS JSON feed](https://gbfs.divvybikes.com/gbfs/en/station_status.json) and count the number of bikes, scooters, and docks currently available.

## Running the Code
First make sure that you have Python3 installed. Then open the terminal and type:
```bash
python3 process_data.py
```

You should get output that looks like this:
```
The Number of Divvy Bikes Currently Available in Chicago: 3695
The Number of Scooters Currently Available in Chicago: 299
The Number of Docks Currently Available in Chicago: 9279
```
