#! /usr/bin/env python

import sys
import requests as r
from functools import reduce
from time import gmtime, strftime

# URL constants 
LOCATION_URL = "http://www.geobytes.com/IpLocator.htm"
WEATHER_URL = "http://api.openweathermap.org/data/2.1/find/name"


def safe_get(critical,*args):
	try:
		return reduce(lambda a,b: a[b], args)
	except KeyError:
		if critical:
			sys.exit("Oops! Corrupted data :(")
		return 'N/A'

def get_location():
	try:
		location = r.get(LOCATION_URL, params={'template':'json.txt'}).json()
	except r.ConnectionError:
		sys.exit("Unable to connect :(")
	country = safe_get(True, location, 'geobytes', 'country')
	city = safe_get(True, location, 'geobytes', 'city')
	return (city, country)

def get_weather_data(city, country, units='metric'):	
	weather_params = {'q':'{0},{1}'.format(city,country), 'units': units}
	weather = r.get(WEATHER_URL, params=weather_params).json()
	w = safe_get(True, weather,'list',0)  #temp var 
	weather_data = {
		'city' : 	safe_get(True, w, 'name'),				 # city and country are retrieved	
		'country' : 	safe_get(True, w, 'sys', 'country'), # again from weather data 
		'date' : 	safe_get(True, w, 'date'),
		'temp' :	round(safe_get(True, w, 'main', 'temp')), 
		'description' :	safe_get(False, w, 'weather', 0, 'description'),
		'windspeed' : 	safe_get(False, w, 'wind', 'speed'),
		'humidity' : 	safe_get(False, w, 'main', 'humidity')
	}
	return weather_data

def output_weather(weather_data):
	current_time = strftime("%Y-%m-%d %H:%M:%S",gmtime())
	print(
	"""
	{0}
	Updated:	{1} GMT
	Time now:	{2} GMT
	---------------------------------------
	Temperature:	{3} (C)
	Wind:		{5} (m/s)
	Humidity:	{6} (%)
	Condition:	{4}
	"""
	.format(
		weather_data['city']+', '+weather_data['country'],
		weather_data['date'],
		current_time,
		weather_data['temp'],
		weather_data['description'],
		weather_data['windspeed'],
		weather_data['humidity']		
		)
	)

def main():
	city,country=get_location()
	weather=get_weather_data(city,country)
	output_weather(weather)

if __name__ == '__main__':
	main()