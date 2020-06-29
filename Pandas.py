import json as json
import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 20)

#Read JSON
data = pd.read_json(r'MoodyRancher.json')

#Convert MPH
def miles_per_hour (dist, speed) :
	speed_in_feet = data['speed'] * 3.28084 * 3600
	speed_in_mph = speed_in_feet / 5280
	return speed_in_mph
data['speed(mph)'] = miles_per_hour(0,0)

# This is where we calulate % gradient during each interval. Version 1.0.0 Highly inaccurate
for row, value in data['altitude'].iteritems():
	print (row, value)
data['rise(meters)'] = data['altitude'].diff()
data['rise(feet)'] = data['altitude'].diff() * 3.28084
data['run(miles)'] = data['distance'].diff()
data['run(feet)'] = data['distance'].diff() * 3.28084
data['gradient(%)'] = data['rise(feet)'] / data['run(feet)'] * 100



#Print DataFrame
print data
	