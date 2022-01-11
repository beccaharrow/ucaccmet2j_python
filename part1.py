import json
with open('precipitation.json', 'r') as precipitation_json:
    precipitation_data = json.load(precipitation_json)

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
precipitation_per_month = []
station_code = "GHCND:US1WAKG0038"
for month in range(12): 
    monthly_total = 0
    for measurement in precipitation_data: 
        date = measurement['date'].split('-')
        date = date[1]
        if measurement['station'] == station_code and date == months[month]: 
            monthly_total = monthly_total + measurement['value'] 
    precipitation_per_month.append(monthly_total)

seattle_data = {
    "station": station_code,
    "state": "WA",
    "total_Monthly_precipitation": precipitation_per_month
}

with open('result1', 'w') as saving_part1: 
    json.dump(seattle_data, saving_part1)
