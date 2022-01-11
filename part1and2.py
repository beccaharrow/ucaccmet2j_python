# answers to part 1 begin here 
import json
with open('precipitation.json', 'r') as precipitation_json:
    precipitation_data = json.load(precipitation_json)

#loops through the different months, and goes through the data finding measurements with the same month and the same station code
#these measurements are added up to create monthly totals
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
precipitation_per_month = []
station_code = "GHCND:US1WAKG0038"
for month in months: 
    #monthly total is reset for each month so that it is not a running total
    monthly_total = 0
    for measurement in precipitation_data: 
        #this creates a variable which gets only the month from the date stores in the json file, which can then be compared to the above list
        date = measurement['date'].split('-')
        date = date[1]
        #measurement is only added to the total if BOTH conditions are met
        if measurement['station'] == station_code and date == month: 
            monthly_total = monthly_total + measurement['value']/10
#the monthly totals are saved to a list 
    precipitation_per_month.append(monthly_total)

#creating a dictionary to be saved in a .json file
seattle_data = {
    "station": station_code, 
    "state": "WA",
    "totalMonthlyPrecipitation": precipitation_per_month
}

with open('result1.json', 'w') as saving_part1: 
    json.dump(seattle_data, saving_part1)
# answers to part 1 end here 

#answers to part 2 begin here 
#loops through the list of monthly totals and adds them together for the yearly total
total_yearly_precipitation = 0 
for monthly_precipitation in precipitation_per_month: 
    total_yearly_precipitation = total_yearly_precipitation + monthly_precipitation

#divides the monthly totals by the yearly totals to obtain the relative values, and saves this to the list
relative_monthly_rainfall = []
for month in range(12): 
    relative_current_month = precipitation_per_month[month]/total_yearly_precipitation
    relative_monthly_rainfall.append(relative_current_month)

#adding these values to the dictionary
seattle_data['realtiveMonthlyPrecipitation'] = relative_monthly_rainfall
seattle_data['totalYearlyPrecipitation'] = total_yearly_precipitation

with open('result2.json', 'w') as saving_part2: 
    json.dump(seattle_data, saving_part2)
# answers to part 2 end here 



