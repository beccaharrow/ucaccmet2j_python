import json
 
location_precipitation_data = []
with open('stations.csv', 'r') as station_data: 
    headers = station_data.readline()
    for station in station_data: 
        location, state, station_code = station.strip().split(",")
        current_location = {'location': location, 'station': station_code, 'state': state}
        location_precipitation_data.append(current_location)
print(location_precipitation_data)

with open('precipitation.json', 'r') as precipitation_json:
    precipitation_data = json.load(precipitation_json)

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
overall_total = 0 
for i in range(len(location_precipitation_data)): 
    yearly_total = 0 
    precipitation_per_month = []
    relative_monthly_rainfall = []
    for measurement in precipitation_data: 
        if measurement['station'] == location_precipitation_data[i]['station']: 
            yearly_total = yearly_total + measurement['value'] 
    for month in range(12):
        monthly_total = 0  
        for measurement in precipitation_data: 
            date = measurement['date'].split('-')
            date = date[1]
            if measurement['station'] == location_precipitation_data[i]['station'] and date == months[month]:
                monthly_total = monthly_total + measurement['value'] 
        relative_current_month = monthly_total/yearly_total
        relative_monthly_rainfall.append(relative_current_month)
        precipitation_per_month.append(monthly_total)
    location_precipitation_data[i]['totalYearlyPrecipitation'] = yearly_total
    location_precipitation_data[i]['totalMonthlyPrecipitation'] = precipitation_per_month
    location_precipitation_data[i]['relativeMonthlyPrecipitation'] = relative_monthly_rainfall
    overall_total = overall_total + yearly_total 

for i in range(len(location_precipitation_data)): 
    relative_yearly_rainfall = location_precipitation_data[i]['totalYearlyPrecipitation']/overall_total
    location_precipitation_data[i]['relativeYearlyPrecipitation'] = relative_yearly_rainfall
    print(location_precipitation_data[i]['relativeYearlyPrecipitation'])





    
