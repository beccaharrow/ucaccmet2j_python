import json
location_precipitation_data = {}
with open('stations.csv', 'r') as station_data: 
    headers = station_data.readline()
    for station in station_data: 
        location, state, station_code = station.strip().split(",")
        location_precipitation_data[location] = {}
        location_precipitation_data[location]['station'] = station_code
        location_precipitation_data[location]['state'] = state

with open('precipitation.json', 'r') as precipitation_json:
    precipitation_data = json.load(precipitation_json)

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
overall_total = 0 
for location in location_precipitation_data: 
    yearly_total = 0 
    precipitation_per_month = []
    relative_monthly_rainfall = []
    for measurement in precipitation_data: 
        if measurement['station'] == location_precipitation_data[location]['station']: 
            yearly_total = yearly_total + measurement['value']/10
    for month in months:
        monthly_total = 0  
        for measurement in precipitation_data: 
            date = measurement['date'].split('-')
            date = date[1]
            if measurement['station'] == location_precipitation_data[location]['station'] and date == month:
                monthly_total = monthly_total + measurement['value']/10
        relative_current_month = monthly_total/yearly_total
        relative_monthly_rainfall.append(relative_current_month)
        precipitation_per_month.append(monthly_total)
    location_precipitation_data[location]['totalMonthlyPrecipitation'] = precipitation_per_month
    location_precipitation_data[location]['relativeMonthlyPrecipitation'] = relative_monthly_rainfall
    location_precipitation_data[location]['totalYearlyPrecipitation'] = yearly_total
    
    overall_total = overall_total + yearly_total 

for location in location_precipitation_data: 
    relative_yearly_rainfall = location_precipitation_data[location]['totalYearlyPrecipitation']/overall_total
    location_precipitation_data[location]['relativeYearlyPrecipitation'] = relative_yearly_rainfall

with open('result3.json', 'w') as saving_part3: 
    json.dump(location_precipitation_data, saving_part3)


