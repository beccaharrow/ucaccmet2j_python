import json

def load_location_data(): 
    location_data = {}
    with open('stations.csv', 'r') as station_data: 
        headers = station_data.readline()
        for station in station_data: 
            location, state, station_code = station.strip().split(",")
            location_data[location] = {}
            location_data[location]["station"] = station_code
            location_data[location]["state"] = state
    print(location_data)

load_location_data()
    
